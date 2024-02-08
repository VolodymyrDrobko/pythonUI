import logging
import sys

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.webdriver import WebDriver

console = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s: %(levelname)s - %(message)s', '%H:%M:%S')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)
logging.getLogger().setLevel(logging.INFO)


def info(message: str) -> None:
    with allure.step("INFO: " + message):
        logging.info(message)


def passed(message: str) -> None:
    log = f"VERIFICATION: {message} - PASSED"
    with allure.step(log):
        logging.info(log)


def attach_screenshot(driver) -> None:
    allure.attach(driver.get_screenshot_as_png(), "screenshot", attachment_type=AttachmentType.PNG)


def warning(driver: WebDriver, message: str) -> None:
    with allure.step("WARNING: " + message):
        attach_screenshot(driver)
        logging.warning(message)


def error(driver: WebDriver, message: str) -> None:
    log = f"VERIFICATION: {message} - FAILED"
    with allure.step(log):
        attach_screenshot(driver)
        logging.error(log)


def db_error(message: str, e: Exception) -> None:
    log = f"DB: {message} - CONNECTION FAILED"
    with allure.step(log):
        logging.error(log, e)
