from pages.PageObject import PageObject


class ListCustomersPage(PageObject):
    # Locators
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject'

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.open_customer_page()
