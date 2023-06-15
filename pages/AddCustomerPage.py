from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.PageObject import PageObject


class AddCustomerPage(PageObject):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def set_first_name(self, first_name):
        self.driver.find_element(By.CSS_SELECTOR, "[ng-model='fName']").send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(By.CSS_SELECTOR, "[ng-model='lName']").send_keys(last_name)

    def set_post_code(self, post_code):
        self.driver.find_element(By.CSS_SELECTOR, "[ng-model='postCd']").send_keys(post_code)

    def click_on_add_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, "[name='myForm'] button").click()

    def set_form_and_click_on_add_customer(self, first_name, last_name, post_code):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_post_code(post_code)
        self.click_on_add_customer()

    def msg_customer_added_sucessfully_displayed(self):
        msg = "Customer added successfully with customer id :"
        return msg in self.wait_alert_is_present().text

    def accept_alert(self):
        self.wait_alert_is_present().accept()

    def is_form_displayed(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[name=myForm]").is_displayed()
