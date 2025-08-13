import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L


class TestAuthentication:
    def test_authentication(self, driver, base_url, create_email):
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
        wait.until(EC.visibility_of_element_located(L.LOGOUT_BUTTON)).click()

    
        wait.until(EC.element_to_be_clickable(L.LOGIN_REG_BUTTON)).click()
        driver.find_element(*L.EMAIL_INPUT).send_keys(email)
        driver.find_element(*L.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*L.LOGIN_BUTTON).click()
        user_name_element = wait.until(EC.visibility_of_element_located(L.USER_NAME))

        assert user_name_element.text == "User.", "Имя пользователя не отображается или неверно"
        assert wait.until(EC.visibility_of_element_located(L.USER_AVATAR)), "Аватар пользователя не найден"

    def test_logout(self, driver, base_url, create_email):
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
        wait.until(EC.visibility_of_element_located(L.LOGOUT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(L.LOGIN_REG_BUTTON))

        assert not driver.find_elements(*L.USER_AVATAR)
        assert not driver.find_elements(*L.USER_NAME)
        assert driver.find_element(*L.LOGIN_REG_BUTTON).is_displayed()
    