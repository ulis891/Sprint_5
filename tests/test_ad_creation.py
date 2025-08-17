from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L


class TesttestAdCreation:
    def test_ad_creation_by_authorized_user(self, driver, base_url, create_email):
        email = create_email
        password = "password123"

        ad = {'title': 'LADA',
              'city': 'Москва',
              'description': 'Седан, баклажан, 2 ядра, 2 колеса',
              'price': '696'}

        driver.get(base_url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(L.LOGIN_REG_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(L.NO_ACCOUNT_BUTTON)).click()
        driver.find_element(*L.EMAIL_INPUT).send_keys(email)
        driver.find_element(*L.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*L.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*L.CREATE_ACCOUNT_BUTTON).click()

        # для того, что бы удостоверится в загрузке страницы
        wait.until(EC.visibility_of_element_located(L.USER_AVATAR))

        wait.until(EC.element_to_be_clickable(L.POST_AD_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(L.AD_TITLE_INPUT)).send_keys(ad['title'])

        driver.find_element(*L.CATEGORY_DROPDOWN).click()
        driver.find_element(*L.CATEGORY_OPTION_AUTO).click()

        radio = driver.find_element(*L.USED_CONDITION_RADIO)
        driver.execute_script("arguments[0].click();", radio)

        driver.find_element(*L.CITY_DROPDOWN).click()
        driver.find_element(*L.CITY_OPTION_MOSCOW).click()

        driver.find_element(*L.AD_DESCRIPTION_INPUT).send_keys(ad['description'])
        driver.find_element(*L.AD_PRICE_INPUT).send_keys(ad['price'])
        driver.find_element(*L.PUBLISH_BUTTON).click()

        wait.until(EC.url_to_be(base_url))
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

    def test_create_ad_not_logged_in(self, driver, base_url):
        expected_text = 'Чтобы разместить объявление, авторизуйтесь'
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(L.POST_AD_BUTTON)).click()
        actual_text = wait.until(EC.visibility_of_element_located(L.MODAL_AUTH_REQUIRED)).text
        assert expected_text == actual_text




