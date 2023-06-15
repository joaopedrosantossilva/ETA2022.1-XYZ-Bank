from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class HomePage(PageObject):
    # Locators
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject'

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.open_home_page()

    def open_home_page(self):
        self.driver.get(self.url)

    def click_on_bank_manager_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "[ng-click='manager()']").click()

    def click_on_customer_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "[ng-click='customer()']").click()

    def click_on_customers(self):
        self.driver.find_element(By.CSS_SELECTOR,"[ng-click='showCust()']").click()


