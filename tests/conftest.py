import pytest
from faker import Faker

from pages.AddCustomerPage import AddCustomerPage
from pages.BankManagerPage import BankManagerPage
from pages.CustomerLoginPage import CustomerLoginPage
from pages.HomePage import HomePage
from pages.OpenAccountPage import OpenAccountPage
from pages.PageObject import PageObject


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Set browser")

@pytest.fixture()
def choose_browser(request):
    selected_browser = request.config.getoption("--browser").lower()
    yield selected_browser

@pytest.fixture()
def open_home(choose_browser):
    home_page = HomePage(browser=choose_browser)
    yield home_page

@pytest.fixture()
def create_customer(open_home):
    # Generation Data
    generator = Faker()
    first_name = generator.unique.first_name()
    last_name = generator.unique.last_name()
    post_code = generator.postcode()
    open_home.click_on_bank_manager_login()
    bank_manager_page = BankManagerPage(open_home.driver)
    bank_manager_page.clicar_em_add_customer()
    add_customer_page = AddCustomerPage(bank_manager_page.driver)
    add_customer_page.set_form_and_click_on_add_customer(first_name, last_name, post_code)
    add_customer_page.accept_alert()
    yield [open_home, first_name,last_name]

@pytest.fixture()
def create_account_with_dollar(create_customer):
    home_page = create_customer[0]
    user = "" + create_customer[1] + " " + create_customer[2]
    home_page.click_on_home_button()
    home_page.click_on_bank_manager_login()
    bank_manager_page = BankManagerPage(home_page.driver)
    bank_manager_page.click_on_open_account()
    open_account_page = OpenAccountPage(bank_manager_page.driver)
    open_account_page.select_customer(user)
    open_account_page.select_currency("Dollar")
    open_account_page.click_on_process()
    open_account_page.accept_alert()
    yield [home_page, user]

