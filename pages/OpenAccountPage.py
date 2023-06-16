from selenium.webdriver.common.by import By
from pages.PageObject import PageObject
from selenium.webdriver.support.select import Select


class OpenAccountPage(PageObject):
    # Locators
    id_select_customer = 'userSelect'
    id_currency = 'currency'
    css_selector_process = "[name=myForm] button"
    msg_account_created = "Account created successfully with account Number :"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def select_customer(self, customer_name):
        element = self.driver.find_element(By.ID, self.id_select_customer)
        Select(element).select_by_visible_text(customer_name)

    def select_currency(self, currency):
        element = self.driver.find_element(By.ID, self.id_currency)
        Select(element).select_by_visible_text(currency)

    def click_on_process(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_process).click()

    def msg_account_created_successfully_displayed(self):
        return self.msg_account_created in self.wait_alert_is_present().text
