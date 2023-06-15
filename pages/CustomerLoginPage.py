from selenium.webdriver.common.by import By
from pages.PageObject import PageObject
from selenium.webdriver.support.select import Select

class CustomerLoginPage(PageObject):
    #locators
    url = "open_customer_Login_by_url"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def select_user(self, user_name):
        element = self.driver.find_element(By.ID, 'userSelect')
        Select(element).select_by_visible_text(user_name)

    def click_on_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "[name=myForm] button").click()
