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
    MODAL_AUTH_REQUIRED = (By.XPATH, '//h1[contains(text(), "Чтобы разместить объявление, авторизуйтесь")]')

    # Форма создания объявления
    AD_TITLE_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    AD_DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[name='description']")
    AD_PRICE_INPUT = (By.CSS_SELECTOR, "input[name='price']")
    CATEGORY_DROPDOWN = (By.XPATH, "//input[@name='category']/following-sibling::button")
    CATEGORY_OPTION_AUTO = (By.XPATH, "//button[span[text()='Авто']]")
    CITY_DROPDOWN = (By.XPATH, "//input[@name='city']/following-sibling::button")
    CITY_OPTION_MOSCOW = (By.XPATH, "//button[span[text()='Москва']]")
    NEW_CONDITION_RADIO = (By.XPATH, "//input[@name='condition' and @value='Новый']")
    USED_CONDITION_RADIO = (By.XPATH, "//input[@name='condition' and @value='Б/У']")
    PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")

    # Мои объявления
    AD_CARD = (By.XPATH, '//div[@class="card"]')
    AD_CARD_TITLE = (By.CSS_SELECTOR, '.card .about h2')
    AD_CARD_CITY = (By.CSS_SELECTOR, '.card .about h3')
    AD_CARD_PRICE = (By.CSS_SELECTOR, "div.card div.price h2.h2")
