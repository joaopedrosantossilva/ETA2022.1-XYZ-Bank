import pytest
from faker import Faker

from pages.AddCustomerPage import AddCustomerPage
from pages.BankManagerPage import BankManagerPage
from pages.HomePage import HomePage
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
    open_home.clicar_em_bank_manager_login()
    bank_manager_page = BankManagerPage(open_home.driver)
    bank_manager_page.clicar_em_add_customer()
    add_customer_page = AddCustomerPage(bank_manager_page.driver)
    add_customer_page.set_form_and_click_on_add_customer(first_name, last_name, post_code)
    add_customer_page.accept_alert()
    home_page = HomePage()
    home_page.click_on_home_button()
    yield [home_page, first_name,last_name]
