from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core import Logger
from page.base.element.web_object import WebObject


class Action:
    DEFAULT_TIMEOUT = 20

    def __init__(self, driver):
        self.driver = driver

    # DECORATES
    def find_element_by_xpath(self, element: WebObject) -> WebElement:
        return self.driver.find_element("xpath", element.xpath)

    # WAIT
    def is_displayed(self, element: WebObject, timeout=1) -> bool:
        try:
            self.wait_for_element(element, timeout)
        except NoSuchElementException:
            return False
        return True

    def wait_for_element(self, element: WebObject, timeout: int) -> None:
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, element.xpath)))

    # TEXT
    def get_text(self, element: WebObject) -> str:
        self.wait_for_element(element, self.DEFAULT_TIMEOUT)
        text = self.find_element_by_xpath(element).text
        Logger.info(f'GET text - {text} - element: [{element.name}]')
        return text

    def set_text(self, element: WebObject, text: str) -> None:
        self.wait_for_element(element, self.DEFAULT_TIMEOUT)
        self.find_element_by_xpath(element).clear()
        self.find_element_by_xpath(element).send_keys(text)
        Logger.info(f"SET text: {text} - element: [{element.name}]")

    # CLICK
    def click_(self, element: WebObject) -> None:
        self.wait_for_element(element, self.DEFAULT_TIMEOUT)
        WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, element.xpath)))
        self.scroll_to_element(element)
        self.find_element_by_xpath(element).click()
        Logger.info(f"CLICK - element: [{element.name}]")

    # IFRAME
    def switch_to_iframe(self, element: WebObject) -> None:
        self.wait_for_element(element, self.DEFAULT_TIMEOUT)
        self.driver.switch_to.frame(self.find_element_by_xpath(element))
        Logger.info(f"SWITCH to iframe: [{element.name}]")

    def switch_to_default_content(self) -> None:
        self.driver.switch_to.default_content()
        Logger.info("SWITCH to default iframe")

    # SCROLL
    def scroll_to_element(self, element: WebObject):
        try:
            ActionChains(self.driver).move_to_element(self.find_element_by_xpath(element)).perform()
            code = ("document.evaluate(\"" + element.xpath +
                    (
                        "\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null)"
                        ".singleNodeValue.scrollIntoView({block: 'center', inline: 'center'})"))
            self.driver.execute_script(code)
        except NoSuchElementException:
            Logger.warning(self.driver, f"Can not scroll to element: [{element.name}]")
