from page.base.base_bo import BasePageBO
from page.pages.main.overview_page import OverviewPage


class OverviewPageBO(BasePageBO):

    def __init__(self, driver):
        super().__init__(driver)
        self.overview_page = OverviewPage(driver)

    def is_my_rewards_window_displayed(self) -> None:
        actual = self.overview_page.is_my_rewards_window_displayed()
        self.soft_assert.assert_(actual == False, "My Reward window is - DISPLAYED")

    def close_my_rewards_window(self) -> None:
        self.overview_page.close_my_rewards_window()

    def is_overview_button_displayed(self) -> None:
        actual = self.overview_page.is_overview_button_displayed()
        self.soft_assert.assert_(actual, "Overview button is - DISPLAYED")
