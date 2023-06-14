from selenium.webdriver.common.by import By
from pages.PageObject import PageObject
from selenium.webdriver.support.select import Select


class OpenAccountPage(PageObject):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def select_customer(self, customer_name):
        element = self.driver.find_element(By.ID, 'userSelect')
        Select(element).select_by_visible_text(customer_name)

    def select_currency(self, currency):
        element = self.driver.find_element(By.ID, 'currency')
        Select(element).select_by_visible_text(currency)

    def click_on_process(self):
        self.driver.find_element(By.CSS_SELECTOR, "[name=myForm] button").click()

    def msg_account_created_sucessfully_displayed(self):
        msg = "Account created successfully with account Number :"
        return msg in self.wait_alert_is_present().text
