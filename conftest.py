import pytest
import selenium.webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from core import Logger


@pytest.fixture(autouse=True)
def driver() -> WebDriver:
    driver = selenium.webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    Logger.attach_screenshot(driver)
    driver.quit()
