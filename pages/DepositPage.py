from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class DepositPage(PageObject):
    # locators
    css_selector_amount_to_be_deposited = "[ng-model='amount']"
    css_selector_msg_deposit_success = "[ng-show='message']"
    msg_deposit_success = "Deposit Successful"
    css_selector_deposit = "[name='myForm'] button"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def amount_to_be_deposited(self, valor):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_amount_to_be_deposited).send_keys(valor)

    def validated_message_deposit_success(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.css_selector_msg_deposit_success).text == self.msg_deposit_success

    def click_on_deposit(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_deposit).click()
