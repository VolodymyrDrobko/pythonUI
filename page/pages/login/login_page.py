from page.base.base_page import BasePage
from page.base.element.web_button import WebButton
from page.base.element.web_input import WebInput
from page.base.element.web_object import WebObject
from utils import Utils


class LoginPage(BasePage):
    SIGN_IN_HEADER = WebObject("//h2[contains(text(),'Sign In')]", "Sign In header")
    ERROR_MESSAGE = WebObject("//div[contains(@class, 'error infobox')]/..//p", "Error message")
    INT_THE_FAQ_LINK = WebObject("//a[contains(text(), 'in the FAQ')]", "FAQ Link")
    UNABLE_TO_LOGIN_HEADER = WebObject("//span[text()='I’m unable to log into my Fizz account. What do I do?']",
                                       "Unable tp login header")
    EMAIL_INPUT = WebInput("//p[text()='Email']/..//input", "Email")
    PASSWORD_INPUT = WebInput("//input[@type='password']", "Password")
    SIGN_IN_BUTTON = WebButton("//input[@value='Sign in']", "Sign In")
    CREATE_YOUR_ACCOUNT_BUTTON = WebButton("//a[contains(text(),'Create your account')]",
                                           "Create your account")
    FORGOT_PASSWORD_BUTTON = WebButton("//a[text()='Forgot password?']", "Forgot password")

    def __init__(self, driver):
        super().__init__(driver)

    def is_sign_in_header_displayed(self) -> bool:
        self.action.wait_for_element(self.SIGN_IN_HEADER, 100)
        return self.action.is_displayed(self.SIGN_IN_HEADER)

    def get_email_error_message(self) -> str:
        return self.action.get_text(self.ERROR_MESSAGE)

    def get_password_error_message(self) -> str:
        message = self.action.get_text(self.ERROR_MESSAGE)
        return Utils.replace_sub_string(r'<a.*>', '', message)

    def click_in_the_FAQ_link(self) -> None:
        self.action.click_(self.INT_THE_FAQ_LINK)

    def navigate_back_to_sign_in_window(self) -> None:
        self.browser.navigate_back()

    def is_unable_to_login_header_displayed(self) -> bool:
        self.action.wait_for_element(self.UNABLE_TO_LOGIN_HEADER, 100)
        return self.action.UNABLE_TO_LOGIN_HEADER.is_displayed(self.UNABLE_TO_LOGIN_HEADER)

    def set_email(self, email: str) -> None:
        self.action.set_text(self.EMAIL_INPUT, email)

    def set_password(self, password: str) -> None:
        self.action.set_text(self.PASSWORD_INPUT, password)

    def click_sign_in(self) -> None:
        self.action.wait_for_element(self.SIGN_IN_BUTTON, 100)
        self.action.click_(self.SIGN_IN_BUTTON)

    def click_forgot_password_button(self) -> None:
        self.action.wait_for_element(self.FORGOT_PASSWORD_BUTTON, 10)
        self.action.click_(self.FORGOT_PASSWORD_BUTTON)

    def click_create_your_account_button(self) -> None:
        self.action.wait_for_element(self.CREATE_YOUR_ACCOUNT_BUTTON, 100)
        self.action.click_(self.CREATE_YOUR_ACCOUNT_BUTTON)
