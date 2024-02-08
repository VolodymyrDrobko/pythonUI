from page.base.base_page import BasePage
from page.base.element.web_button import WebButton
from page.base.element.web_input import WebInput
from page.base.element.web_object import WebObject


class CreateAccountPage(BasePage):
    HEADER = WebObject("//h2[text()='Create your account']", "Create your account header")
    EMAIL_INPUT = WebInput("//input[@name='userProfile.email']", "Email")
    FIRST_NAME_INPUT = WebInput("//input[@name='userProfile.firstName']", "First name")
    LAST_NAME_INPUT = WebInput("//input[@name='userProfile.lastName']", "Last name")
    PASSWORD_INPUT = WebInput("//input[@name='credentials.passcode']", "Password")
    CREATE_MY_ACCOUNT_BUTTON = WebButton("//input[@value='Create my account ']/..", "Create my Account")

    def __init__(self, driver):
        super().__init__(driver)

    def is_create_account_header_displayed(self) -> bool:
        return self.action.is_displayed(self.HEADER, 10)

    def set_email(self, email: str) -> None:
        self.action.set_text(self.EMAIL_INPUT, email)

    def set_first_name(self, first_name: str) -> None:
        self.action.set_text(self.FIRST_NAME_INPUT, first_name)

    def set_last_name(self, last_name: str) -> None:
        self.action.set_text(self.LAST_NAME_INPUT, last_name)

    def set_password(self, password: str) -> None:
        self.action.set_text(self.PASSWORD_INPUT, password)

    def click_create_my_account_button(self) -> None:
        self.action.wait_for_element(self.CREATE_MY_ACCOUNT_BUTTON, 10)
        self.action.click_(self.CREATE_MY_ACCOUNT_BUTTON)
