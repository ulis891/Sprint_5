import pytest
from selenium import webdriver
import time


@pytest.fixture
def base_url():
    return "https://qa-desk.stand.praktikum-services.ru/"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def create_email():
    return f"test_{int(time.time())}@praktikum.test"
