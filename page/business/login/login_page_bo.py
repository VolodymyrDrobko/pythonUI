from page.base.base_bo import BasePageBO
from page.pages.login.login_page import LoginPage


class LoginPageBO(BasePageBO):

    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPage(driver)

    def is_sign_in_header_displayed(self) -> None:
        actual = self.login_page.is_sign_in_header_displayed()
        self.soft_assert.assert_(actual, "Sign In header - is DISPLAYED")

    def click_create_your_account_button(self) -> None:
        self.login_page.click_create_your_account_button()
