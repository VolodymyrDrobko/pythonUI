from page.base.base_page import BasePage
from page.base.element.web_button import WebButton
from page.base.element.web_input import WebInput


class MagicCodeConfirmationPage(BasePage):
    MAGIC_CODE_INPUT = WebInput("//input[@name='credentials.passcode']", "Magic Code")
    VERIFY_BUTTON = WebButton("//input[@value='Verify']", "Verify")

    def __init__(self, driver):
        super().__init__(driver)

    def is_magic_code_input_displayed(self) -> bool:
        return self.action.is_displayed(self.MAGIC_CODE_INPUT, 30)

    def set_magic_code(self, magic_code: str) -> None:
        self.action.wait_for_element(self.MAGIC_CODE_INPUT, 20)
        return self.action.set_text(self.MAGIC_CODE_INPUT, magic_code)

    def click_verify_button(self) -> None:
        self.action.wait_for_element(self.VERIFY_BUTTON, 20)
        self.action.click_(self.VERIFY_BUTTON)
