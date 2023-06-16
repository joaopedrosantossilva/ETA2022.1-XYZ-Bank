from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class AccountPage(PageObject):

    #locators
    css_selector_msg_welcome = "span[class='fontBig ng-binding']"
    css_selector_msg_please_an_account = "[ng-show='noAccount']"
    css_selector_deposit = "[ng-click='deposit()']"
    css_selector_value_balance = ".ng-scope [ng-hide=noAccount] .ng-binding:nth-child(2)"
    css_selector_withdrawl = "[ng-click='withdrawl()']"
    css_selector_transactions = "[ng-click='transactions()']"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_msg_welcome_user_displayed(self, user):
        return self.driver.find_element(By.CSS_SELECTOR, self.css_selector_msg_welcome).text == user

    def is_msg_please_open_an_account_displayed(self):
        msg = "Please open an account with us."
        return self.driver.find_element(By.CSS_SELECTOR,self.css_selector_msg_please_an_account).text == msg

    def click_on_deposit(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_deposit).click()

    def is_value_balance(self, value):
        return self.driver.find_element(By.CSS_SELECTOR, self.css_selector_value_balance).text == value

    def click_on_withdrawl(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_withdrawl).click()

    def click_on_transactions(self):
        self.driver.find_element(By.CSS_SELECTOR,self.css_selector_transactions).click()