from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L

class TesttestAdCreation:
    def test_ad_creation_by_authorized_user(self, driver, base_url, create_email):
        email = create_email
        password = "password123"

        driver.get(base_url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(L.LOGIN_REG_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(L.NO_ACCOUNT_BUTTON)).click()
        driver.find_element(*L.EMAIL_INPUT).send_keys(email)
        driver.find_element(*L.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*L.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*L.CREATE_ACCOUNT_BUTTON).click()

        wait.until(EC.visibility_of_element_located(L.POST_AD_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(L.AD_TITLE_INPUT)).send_keys('LADA')
        



