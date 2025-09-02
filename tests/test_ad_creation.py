from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L
from data import TestData as D


class TestAdCreation:
    def test_ad_creation_by_authorized_user_success(self, driver):
        email = D.TEST_USER_EMAIL
        password = D.TEST_USER_PASSWORD
        driver.get(D.BASE_URL)
        wait = WebDriverWait(driver, D.WAIT_TIME)
        ad = {
            'title': D.AD_TITLE,
            'city': D.AD_CITY,
            'description': D.AD_DESCRIPTION,
            'price': D.AD_PRICE
            }

        wait.until(EC.element_to_be_clickable(L.LOGIN_REG_BUTTON)).click()
        driver.find_element(*L.EMAIL_INPUT).send_keys(email)
        driver.find_element(*L.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*L.LOGIN_BUTTON).click()

        # для того, что бы удостоверится в загрузке страницы
        wait.until(EC.visibility_of_element_located(L.USER_AVATAR))

        wait.until(EC.element_to_be_clickable(L.POST_AD_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(L.AD_TITLE_INPUT)).send_keys(D.AD_TITLE)

        driver.find_element(*L.CATEGORY_DROPDOWN).click()
        driver.find_element(*L.CATEGORY_OPTION_AUTO).click()

        radio = driver.find_element(*L.USED_CONDITION_RADIO)
        driver.execute_script("arguments[0].click();", radio)

        driver.find_element(*L.CITY_DROPDOWN).click()
        driver.find_element(*L.CITY_OPTION_MOSCOW).click()

        driver.find_element(*L.AD_DESCRIPTION_INPUT).send_keys(D.AD_DESCRIPTION)
        driver.find_element(*L.AD_PRICE_INPUT).send_keys(D.AD_PRICE)
        driver.find_element(*L.PUBLISH_BUTTON).click()

        wait.until(EC.url_to_be(D.BASE_URL))
        wait.until(EC.element_to_be_clickable(L.USER_AVATAR)).click()
        wait.until(EC.visibility_of_element_located(L.AD_CARD))

        title_elem = wait.until(EC.visibility_of_element_located(L.AD_CARD_TITLE))
        city_elem = wait.until(EC.visibility_of_element_located(L.AD_CARD_CITY))
        price_elem = wait.until(EC.visibility_of_element_located(L.AD_CARD_PRICE))

        actual_ad = {
            'title': title_elem.text,
            'city': city_elem.text,
            'price': price_elem.text.split()[0]
        }

        for parameter in actual_ad:
            assert ad[parameter] == actual_ad[parameter]

    def test_create_ad_not_logged_in(self, driver):
        expected_text = 'Чтобы разместить объявление, авторизуйтесь'
        driver.get(D.BASE_URL)
        wait = WebDriverWait(driver, D.WAIT_TIME)
        wait.until(EC.element_to_be_clickable(L.POST_AD_BUTTON)).click()
        actual_text = wait.until(EC.visibility_of_element_located(L.MODAL_AUTH_REQUIRED)).text
        assert expected_text == actual_text
