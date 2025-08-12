import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def base_url():
    return "https://qa-desk.stand.praktikum-services.ru/"
