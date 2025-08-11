from selenium.webdriver.common.by import By


class Locators:
    # Главная страница
    LOGIN_REG_BUTTON = (By.XPATH, '//button[contains(text(), "Вход и регистрация")]')
    POST_AD_BUTTON = (By.XPATH, '//button[contains(text(), "Разместить объявление")]')
    USER_AVATAR = (By.CLASS_NAME, 'user-avatar')
    USER_NAME = (By.CLASS_NAME, 'user-name')
    LOGOUT_BUTTON = (By.XPATH, '//button[contains(text(), "Выйти")]')
    PROFILE_LINK = (By.LINK_TEXT, 'Профиль')

    # Форма авторизации
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')

    # Форма регистрации
    NO_ACCOUNT_BUTTON = (By.XPATH, '//button[contains(text(), "Нет аккаунта")]')
    NAME_INPUT = (By.ID, 'name')
    CONFIRM_PASSWORD_INPUT = (By.ID, 'confirmPassword')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[contains(text(), "Создать аккаунт")]')

    # Ошибки
    ERROR_MESSAGE_UNDER_EMAIL = (By.XPATH, '//input[@id="email"]/following-sibling::span[contains(text(), "Ошибка")]')

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
