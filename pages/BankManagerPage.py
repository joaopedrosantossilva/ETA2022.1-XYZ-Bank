from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.PageObject import PageObject


class BankManagerPage(PageObject):

    #locators
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"
    css_selector_add_customer = "[ng-click='addCust()']"
    css_selector_customers = "[ng-click='showCust()']"
    css_selector_open_account = "[ng-click='openAccount()']"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def clicar_em_add_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_add_customer).click()

    def click_on_customers(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_customers).click()

    def click_on_open_account(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_open_account).click()

    def is_url_page(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.url_to_be(self.url))
        return self.is_url(self.url)
