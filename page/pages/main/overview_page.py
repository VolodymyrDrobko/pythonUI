from page.base.base_page import BasePage
from page.base.element.web_button import WebButton
from page.base.element.web_object import WebObject


class OverviewPage(BasePage):

    MY_REWORDS_POP_UP_WINDOW = WebObject("//div[contains(@class,'dizz-card-lg card--noshadow')]", "My rewords window")
    CLOSE_BUTTON = WebObject("//dizz-icons[@aria-label='Close']", "Close")
    OVERVIEW_BUTTON = WebButton("//span[contains(text(),'Overview')]/..", "Overview")
    LOGOUT_BUTTON = WebButton("//span[@id='logout']/..", "Logout")

    def __init__(self, driver):
        super().__init__(driver)

    def is_my_rewards_window_displayed(self) -> bool:
        self.action.wait_for_element(self.MY_REWORDS_POP_UP_WINDOW, 30)
        return self.action.is_displayed(self.MY_REWORDS_POP_UP_WINDOW)

    def close_my_rewards_window(self) -> None:
        self.action.wait_for_element(self.CLOSE_BUTTON, 20)
        self.action.click_(self.CLOSE_BUTTON)

    def is_overview_button_displayed(self) -> bool:
        self.action.wait_for_element(self.OVERVIEW_BUTTON, 20)
        return self.action.is_displayed(self.OVERVIEW_BUTTON)

    def click_logout(self) -> None:
        self.action.wait_for_element(self.LOGOUT_BUTTON, 50)
        self.action.click_(self.LOGOUT_BUTTON)

