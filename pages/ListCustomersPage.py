from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class ListCustomersPage(PageObject):
    # locators
    tag_name_table_with_list_of_customers = 'table'
    css_selector_search_customer = "[ng-model='searchCustomer']"
    css_selector_delete = "[ng-click='deleteCust(cust)']"
    xpath_list_first_name = "//table/tbody/tr/td[1]"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_table_with_list_of_customers_displayed(self):
        return self.driver.find_element(By.TAG_NAME, self.tag_name_table_with_list_of_customers).is_displayed()

    def search_customer(self, valor):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_search_customer).send_keys(valor)

    def click_on_delete(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_delete).click()

    def clear_search_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_selector_search_customer).clear()

    def the_name_is_no_longer_on_the_customer_list(self, first_name):
        names = self.get_list_first_name()
        result = False
        for name in names:
            if name.text == first_name:
                result = False
                break
            else:
                result = True
        return result

    def get_list_first_name(self):
        return self.driver.find_elements(By.XPATH, self.xpath_list_first_name)
