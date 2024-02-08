from page.base.base_page import BasePage
from page.base.element.web_button import WebButton
from core import config


class HomePage(BasePage):
    MY_ACCOUNT_BUTTON = WebButton("//div[@class='dizz-btn-container d-sm-inline-block d-none']", "My Account")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_home_page(self) -> None:
        self.browser.navigate(config.get_url())

    def is_my_account_button_displayed(self) -> bool:
        return self.action.is_displayed(self.MY_ACCOUNT_BUTTON, 20)

    def click_my_account_button(self) -> None:
        self.action.wait_for_element(self.MY_ACCOUNT_BUTTON, 20)
        self.action.click_(self.MY_ACCOUNT_BUTTON)
