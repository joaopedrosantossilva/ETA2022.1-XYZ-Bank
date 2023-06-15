from selenium.webdriver.common.by import By
from pages.PageObject import PageObject

class DepositPage(PageObject):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def amount_to_be_deposited(self, valor):
        self.driver.find_element(By.CSS_SELECTOR, "[ng-model='amount']").send_keys(valor)

    def validated_message_deposit_success(self):
        msg = "Deposit Successful"
        return self.driver.find_element(By.CSS_SELECTOR, "[ng-show='message']").text == msg

    def click_on_deposit(self):
        self.driver.find_element(By.CSS_SELECTOR, "[name='myForm'] button").click()
