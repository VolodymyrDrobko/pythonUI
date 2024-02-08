from page.base.base_page import BasePage
from page.base.element.web_button import WebButton
from page.base.element.web_input import WebInput
from page.base.element.web_object import WebObject
from core import config


class YopMailPage(BasePage):
    EMAIL_INPUT = WebInput("//input[@id='login']", "Email")
    CHECK_INBOX_ARROW_BUTTON = WebButton("//div[@id='refreshbut']", "Check inbox arrow")
    INBOX_IFRAME = WebObject("//iframe[@id='ifmail']", "Inbox iframe")
    MAGIC_CODE = WebObject("//td[contains(text(),'magic')]//span[contains(text(),'')]", "Magic code")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_yop_mail_page(self) -> None:
        self.browser.open_new_tab_by_url(config.get_yop_mail_url())

    def switch_to_yop_mail_tab(self) -> None:
        self.browser.switch_to_new_tab()

    def set_email(self, email: str) -> None:
        self.action.wait_for_element(self.EMAIL_INPUT, 20)
        self.action.set_text(self.EMAIL_INPUT, email)

    def click_check_inbox_arrow_button(self) -> None:
        self.action.wait_for_element(self.CHECK_INBOX_ARROW_BUTTON, 20)
        self.action.click_(self.CHECK_INBOX_ARROW_BUTTON)

    def switch_to_inbox_iframe(self) -> None:
        self.action.switch_to_iframe(self.INBOX_IFRAME)

    def switch_to_default_iframe_yop_mail_page(self) -> None:
        self.action.switch_to_default_content()

    def get_magic_code(self) -> str:
        self.action.wait_for_element(self.MAGIC_CODE, 20)
        magicCode = self.action.get_text(self.MAGIC_CODE)
        return magicCode

    def close_yop_mail_window(self) -> None:
        self.browser.close_tab()
