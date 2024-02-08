from page.base.base_bo import BasePageBO
from page.pages.yop_mail.yop_mail_page import YopMailPage


class YopMailPageBO(BasePageBO):

    def __init__(self, driver):
        super().__init__(driver)
        self.yop_mail_page = YopMailPage(driver)

    def navigate_to_yop_mail_page(self) -> None:
        self.yop_mail_page.navigate_to_yop_mail_page()
        self.yop_mail_page.switch_to_yop_mail_tab()

    def set_email(self, email: str) -> None:
        self.yop_mail_page.set_email(email)

    def click_check_inbox_arrow_button(self) -> None:
        self.yop_mail_page.click_check_inbox_arrow_button()

    def get_magic_code(self) -> str:
        self.yop_mail_page.switch_to_inbox_iframe()
        magic_code = self.yop_mail_page.get_magic_code()
        self.yop_mail_page.switch_to_default_iframe_yop_mail_page()
        return magic_code
