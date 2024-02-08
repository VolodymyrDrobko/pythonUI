from page.base.base_bo import BasePageBO
from page.pages.login.home_page import HomePage


class HomePageBO(BasePageBO):

    def __init__(self, driver):
        super().__init__(driver)
        self.page = HomePage(driver)

    def navigate_to_home_page(self) -> None:
        self.page.navigate_to_home_page()

    def is_my_account_button_displayed(self) -> None:
        actual = self.page.is_my_account_button_displayed()
        self.soft_assert.assert_(actual, "My account button is - DISPLAYED")

    def click_my_account_button(self) -> None:
        self.page.click_my_account_button()
