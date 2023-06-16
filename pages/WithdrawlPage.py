import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.PageObject import PageObject


class WithdrawlPage(PageObject):
    # Locators
    css_select_amount = "[ng-model=amount]"
    msg_transaction_failed = "Transaction Failed. You can not withdraw amount more than the balance."
    css_selector_msg_transaction_failed = "[ng-show=message]"
    css_selector_withdrawal = "[name='myForm'] button"
    msg_transaction_successful = "Transaction successful"
    css_selector_msg_transaction_successful = "[ng-show='message']"
    txt_amount_to_be_withdrawn = "Amount to be Withdrawn :"
    xpath_txt_amount_to_be_withdrawn = "//div[label='Amount to be Withdrawn :']/label"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def set_amount(self, value):
        self.driver.find_element(By.CSS_SELECTOR, self.css_select_amount).send_keys(value)

    def is_msg_transaction_failed_displayed(self):
        return self.driver.find_element(By.CSS_SELECTOR,
                                        self.css_selector_msg_transaction_failed).text == self.msg_transaction_failed

    def send_withdrawl(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_withdrawal).click()

    def is_msg_transaction_success_displayed(self):
        return self.driver.find_element(By.CSS_SELECTOR,
                                        self.css_selector_msg_transaction_successful).text == self.msg_transaction_successful

    def validated_tela_withdrawl(self):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.xpath_txt_amount_to_be_withdrawn)))
        return self.driver.find_element(By.XPATH,
                                        self.xpath_txt_amount_to_be_withdrawn).text == self.txt_amount_to_be_withdrawn
