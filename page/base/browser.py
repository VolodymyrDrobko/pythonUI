from core import Logger


class Browser:

    def __init__(self, driver):
        self.driver = driver

    # NAVIGATION
    def navigate(self, url: str) -> None:
        Logger.info(f"Navigate to - {url}")
        self.driver.get(url)

    def navigate_back(self) -> None:
        self.driver.execute_script("window.history.go(-1)")
        Logger.info("Navigate BACK in browser")

    # TAB
    def open_new_tab_by_url(self, url: str) -> None:
        self.driver.execute_script("window.open('{}', '_blank');".format(url))
        Logger.info(f"Open new tab and navigate to {url}")

    def switch_tab(self, index: int) -> None:
        new_tab = self.driver.window_handles[index]
        self.driver.switch_to.window(new_tab)
        Logger.info(f"SWITCH to tab: {index}")

    def switch_to_new_tab(self) -> None:
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
        Logger.info(f"SWITCH to NEW tab")

    def switch_to_first_tab(self) -> None:
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[0])
        Logger.info("SWITCH to First tab")

    def close_tab(self) -> None:
        self.driver.close()
        Logger.info("Tab is - CLOSED")
