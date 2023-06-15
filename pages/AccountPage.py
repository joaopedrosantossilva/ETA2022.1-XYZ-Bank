from selenium.webdriver.common.by import By

from pages.PageObject import PageObject

class AccountPage(PageObject):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_msg_welcome_user_displayed(self, user):
        return self.driver.find_element(By.CSS_SELECTOR, "span[class='fontBig ng-binding']").text == user

    def is_msg_plese_open_an_account_displayed(self):
        msg = "Please open an account with us."
        return self.driver.find_element(By.CSS_SELECTOR, "[ng-show='noAccount']").text == msg

