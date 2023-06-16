from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class AddCustomerPage(PageObject):

    #Locators
    css_selector_first_name = "[ng-model='fName']"
    css_selector_last_name = "[ng-model='lName']"
    css_selector_post_code = "[ng-model='postCd']"
    css_selector_add_customer = "[name='myForm'] button"
    msg_successfully_added_customer = "Customer added successfully with customer id :"
    css_selector_form = "[name=myForm]"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def set_first_name(self, first_name):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_first_name).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_last_name).send_keys(last_name)

    def set_post_code(self, post_code):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_post_code).send_keys(post_code)

    def click_on_add_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_add_customer).click()

    def set_form_and_click_on_add_customer(self, first_name, last_name, post_code):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_post_code(post_code)
        self.click_on_add_customer()

    def msg_customer_added_sucessfully_displayed(self):
        return self.msg_successfully_added_customer in self.wait_alert_is_present().text

    def is_form_displayed(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.css_selector_form).is_displayed()
