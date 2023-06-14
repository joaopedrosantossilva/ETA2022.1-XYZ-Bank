from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class BankManagerPage(PageObject):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def clicar_em_add_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, "[ng-click='addCust()']").click()

    def click_on_customers(self):
        self.driver.find_element(By.CSS_SELECTOR, "[ng-click='showCust()']").click()

    def click_on_open_account(self):
        self.driver.find_element(By.CSS_SELECTOR, "[ng-click='openAccount()']").click()