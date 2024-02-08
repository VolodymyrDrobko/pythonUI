from page.base.action import Action
from page.base.browser import Browser


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.action = Action(driver)
        self.browser = Browser(driver)
