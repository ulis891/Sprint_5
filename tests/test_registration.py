import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as L


class TestRegistration:

    def test_user_registration_success(self, driver, base_url):
        unique_email = f"test_{int(time.time())}@praktikum.test"
        password = "password123"

        driver.get(base_url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(L.LOGIN_REG_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(L.NO_ACCOUNT_BUTTON)).click()
        driver.find_element(*L.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*L.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*L.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*L.CREATE_ACCOUNT_BUTTON).click()
        user_name_element = wait.until(EC.visibility_of_element_located(L.USER_NAME))

        assert user_name_element.text == "User.", "Имя пользователя не отображается или неверно"
        assert wait.until(EC.visibility_of_element_located(L.USER_AVATAR)), "Аватар пользователя не найден"

    def test_registration_with_invalid_email_mask_fail(self, driver, base_url):
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(L.LOGIN_REG_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(L.NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(L.EMAIL_INPUT)).send_keys("invalid-email")
        driver.find_element(*L.CREATE_ACCOUNT_BUTTON).click()
        error_elements = wait.until(EC.presence_of_all_elements_located(L.ERROR_ELEMENT))
        error_message = driver.find_element(*L.ERROR_MESSAGE_UNDER_EMAIL).text
        assert len(error_elements) == 3, "Не найдено 3 окна с ошибкой"
        assert error_message == "Ошибка", "Сообщение об ошибке не появилось"

    def test_registration_of_existing_user_fail(self, driver, base_url):
        def registration(web_driver, wait_driver, email, password):
            wait_driver.until(EC.element_to_be_clickable(L.LOGIN_REG_BUTTON)).click()
            wait_driver.until(EC.element_to_be_clickable(L.NO_ACCOUNT_BUTTON)).click()
            web_driver.find_element(*L.EMAIL_INPUT).send_keys(email)
            web_driver.find_element(*L.PASSWORD_INPUT).send_keys(password)
            web_driver.find_element(*L.CONFIRM_PASSWORD_INPUT).send_keys(password)
            web_driver.find_element(*L.CREATE_ACCOUNT_BUTTON).click()

        unique_email = f"test_{int(time.time())}@praktikum.test"
        unique_password = "password123"
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)

        registration(driver, wait, unique_email, unique_password)
        wait.until(EC.element_to_be_clickable(L.LOGOUT_BUTTON)).click()
        registration(driver, wait, unique_email, unique_password)

        error_elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(L.ERROR_ELEMENT))
        error_message = driver.find_elements(*L.ERROR_MESSAGE_UNDER_EMAIL)[0].text
        assert len(error_elements) == 3, "Не найдено 3 окна с ошибкой"
        assert error_message == "Ошибка", "Сообщение об ошибке не появилось"
