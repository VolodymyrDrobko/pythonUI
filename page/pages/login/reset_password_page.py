from page.base.base_page import BasePage
from page.base.element.web_button import WebButton
from page.base.element.web_input import WebInput
from page.base.element.web_object import WebObject


class ResetPasswordPage(BasePage):
    RESET_PASSWORD_HEADER = WebObject("//h2[text()='Reset your password']", "Reset your password header")
    EMAIL_INPUT = WebInput("//input[@name='identifier']", "Email")
    NEXT_BUTTON = WebButton("//input[@type='submit']", "Next")
    MAGIC_NUMER_INPUT = WebInput("//input[@name='credentials.passcode']", "Magic number")
    NEW_PASSWORD_INPUT = WebInput("//label[contains(text(), 'New password')]/../..//input", "New password")
    RE_ENTER_PASSWORD_INPUT = WebInput("//label[contains(text(), 'Re-enter password')]/../..//input",
                                       "Re-enter password")
    RESET_PASSWORD_BUTTON = WebButton("//input[@value='Reset Password']", "Reset Password")

    def __init__(self, driver):
        super().__init__(driver)

    def is_reset_password_header_displayed(self) -> bool:
        self.action.wait_for_element(self.RESET_PASSWORD_HEADER, 50)
        return self.action.is_displayed(self.RESET_PASSWORD_HEADER)

    def set_email(self, email: str) -> None:
        self.action.set_text(self.EMAIL_INPUT, email)

    def click_next_button(self) -> None:
        self.action.wait_for_element(self.NEXT_BUTTON, 10)
        self.action.click_(self.NEXT_BUTTON)

    def wait_for_magic_code_number_input_displayed(self) -> None:
        self.action.wait_for_element(self.MAGIC_NUMER_INPUT, 20)

    def close_reset_password_tab(self) -> None:
        self.browser.close_tab()

    def switch_to_reset_password_tab(self, tabNumber: int) -> None:
        self.browser.switch_tab(tabNumber)

    def set_new_password(self, password: str) -> None:
        self.action.wait_for_element(self.NEW_PASSWORD_INPUT, 50)
        self.action.set_text(self.NEW_PASSWORD_INPUT, password)

    def set_re_enter_password(self, password: str) -> None:
        self.action.wait_for_element(self.RE_ENTER_PASSWORD_INPUT, 20)
        self.action.set_text(self.RE_ENTER_PASSWORD_INPUT, password)

    def click_reset_password(self) -> None:
        self.action.wait_for_element(self.RE_ENTER_PASSWORD_INPUT, 20)
        self.action.click_(self.RESET_PASSWORD_BUTTON)
