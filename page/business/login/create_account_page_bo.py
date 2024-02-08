from page.base.base_bo import BasePageBO
from page.pages.login.create_account_page import CreateAccountPage


class CreateAccountPageBO(BasePageBO):

    def __init__(self, driver):
        super().__init__(driver)
        self.create_account_page = CreateAccountPage(driver)

    def is_create_account_header_displayed(self) -> None:
        actual = self.create_account_page.is_create_account_header_displayed()
        self.soft_assert.assert_(actual == False, "Create Account header - is DISPLAYED")

    def set_email(self, email: str) -> None:
        self.create_account_page.set_email(email)

    def set_first_name(self, first_name: str) -> None:
        self.create_account_page.set_first_name(first_name)

    def set_last_name(self, last_name: str) -> None:
        self.create_account_page.set_last_name(last_name)

    def set_password(self, password: str) -> None:
        self.create_account_page.set_password(password)

    def click_create_my_account_button(self) -> None:
        self.create_account_page.click_create_my_account_button()
