from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class WithdrawlPage(PageObject):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def set_amount(self, value):
        self.driver.find_element(By.CSS_SELECTOR, "[ng-model=amount]").send_keys(value)

    def is_msg_transaction_failed_displayed(self):
        msg = "Transaction Failed. You can not withdraw amount more than the balance."
        return self.driver.find_element(By.CSS_SELECTOR, "[ng-show=message]").text == msg

    def send_withdraw(self):
        self.driver.find_element(By.CSS_SELECTOR, "[name='myForm'] button").click()
