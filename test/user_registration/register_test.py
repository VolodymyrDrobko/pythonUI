import allure
import pytest

from page.base.base_bo import BasePageBO
from page.base.browser import Browser
from page.business.login.create_account_page_bo import CreateAccountPageBO
from page.business.login.home_page_bo import HomePageBO
from page.business.login.login_page_bo import LoginPageBO
from page.business.login.magic_code_confirmation_page_bo import MagicCodeConfirmationPageBO
from page.business.login.yop_mail_page_bo import YopMailPageBO
from page.business.main.overview_page_bo import OverviewPageBO
from utils import RandomGenerator


@allure.suite("Regression")
@allure.feature("Registration")
@allure.title("ABC-111111")
@allure.description("User Registration")
@pytest.mark.regression
@pytest.mark.login
def test_register_user_FBL_10157(driver):
    email = RandomGenerator.get_email()
    first_name = RandomGenerator.get_string(5)
    last_name = RandomGenerator.get_string(5)
    password = RandomGenerator.get_password()

    browser = Browser(driver)
    home_page = HomePageBO(driver)
    login_page = LoginPageBO(driver)
    create_account_page = CreateAccountPageBO(driver)
    yop_mail_page = YopMailPageBO(driver)
    magic_code_confirmation_page = MagicCodeConfirmationPageBO(driver)
    overview_page = OverviewPageBO(driver)

    home_page.navigate_to_home_page()
    home_page.click_my_account_button()
    login_page.is_sign_in_header_displayed()
    login_page.click_create_your_account_button()
    create_account_page.is_create_account_header_displayed()
    create_account_page.set_email(email)
    create_account_page.set_first_name(first_name)
    create_account_page.set_last_name(last_name)
    create_account_page.set_password(password)
    create_account_page.click_create_my_account_button()
    magic_code_confirmation_page.is_magic_code_input_displayed()

    yop_mail_page.navigate_to_yop_mail_page()
    yop_mail_page.set_email(email)
    yop_mail_page.click_check_inbox_arrow_button()
    magic_code = yop_mail_page.get_magic_code()
    browser.close_tab()
    browser.switch_to_first_tab()

    magic_code_confirmation_page.set_magic_code(magic_code)
    magic_code_confirmation_page.click_verify_button()

    overview_page.is_my_rewards_window_displayed()
    overview_page.close_my_rewards_window()
    overview_page.is_overview_button_displayed()

    # soft_assert object should be static to gather all assert fails from project, now it will do it only for login page
    login_page.assert_all()
