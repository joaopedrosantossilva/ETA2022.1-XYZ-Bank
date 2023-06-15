from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class PageObject:
    class_title = 'title'

    def __init__(self, driver=None, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                service = Service(executable_path=ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=service)
            elif browser == 'firefox':
                service = Service(executable_path=GeckoDriverManager().install())
                self.driver = webdriver.Firefox(service=service)
            else:
                raise Exception('Browser não supportado!!')
            self.driver.implicitly_wait(15)
            self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def is_url(self, url):
        return self.driver.current_url == url

    def wait_alert_is_present(self):
        alert = WebDriverWait(self.driver, 15).until(expected_conditions.alert_is_present())
        return alert
    def accept_alert(self):
        self.wait_alert_is_present().accept()

    def click_on_home_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "[ng-click='home()']").click()


