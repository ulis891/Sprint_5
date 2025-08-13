from selenium.webdriver.common.by import By


class Locators:
    # Главная страница
    LOGIN_REG_BUTTON = (By.XPATH, '//button[contains(text(), "Вход и регистрация")]')
    POST_AD_BUTTON = (By.XPATH, '//button[contains(text(), "Разместить объявление")]')
    USER_AVATAR = (By.CLASS_NAME, 'circleSmall')
    USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    LOGOUT_BUTTON = (By.XPATH, '//button[contains(text(), "Выйти")]')
    PROFILE_LINK = (By.LINK_TEXT, 'Профиль')

    # Форма регистрации
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='submitPassword']")
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')
    NO_ACCOUNT_BUTTON = (By.XPATH, '//button[contains(text(), "Нет аккаунта")]')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[contains(text(), "Создать аккаунт")]')

    # Ошибки
    ERROR_MESSAGE_UNDER_EMAIL = (By.CLASS_NAME, 'input_span__yWPqB')
    ERROR_ELEMENT = (By.CLASS_NAME, "input_inputError__fLUP9")

    # Модальное окно
    MODAL_AUTH_REQUIRED = (By.XPATH, '//h2[contains(text(), "Чтобы разместить объявление, авторизуйтесь")]')

    # Форма создания объявления
    AD_TITLE_INPUT = (By.ID, 'title')
    AD_DESCRIPTION_INPUT = (By.ID, 'description')
    AD_PRICE_INPUT = (By.ID, 'price')
    CATEGORY_DROPDOWN = (By.ID, 'category')
    CITY_DROPDOWN = (By.ID, 'city')
    CONDITION_RADIO_NEW = (By.XPATH, '//input[@type="radio" and @value="new"]')
    PUBLISH_BUTTON = (By.XPATH, '//button[contains(text(), "Опубликовать")]')

    # Мои объявления
    MY_ADS_SECTION = (By.XPATH, '//h3[contains(text(), "Мои объявления")]')
