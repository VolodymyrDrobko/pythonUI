from page.base.base_bo import BasePageBO
from page.pages.login.magic_code_confirmation_page import MagicCodeConfirmationPage


class MagicCodeConfirmationPageBO(BasePageBO):

    def __init__(self, driver):
        super().__init__(driver)
        self.page = MagicCodeConfirmationPage(driver)

    def is_magic_code_input_displayed(self) -> None:
        actual = self.page.is_magic_code_input_displayed()
        self.soft_assert.assert_(actual == False, "Magic Code input is - DISPLAYED")

    def set_magic_code(self, magic_code: str) -> None:
        self.page.set_magic_code(magic_code)

    def click_verify_button(self) -> None:
        self.page.click_verify_button()
