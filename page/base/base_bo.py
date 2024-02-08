from core.soft_assert import SoftAssert


class BasePageBO:

    def __init__(self, driver):
        self.driver = driver
        self.soft_assert = SoftAssert(driver)

    def assert_all(self):
        self.soft_assert.verify_expectations(self.driver)
