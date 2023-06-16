from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.PageObject import PageObject


class TransactionsPage(PageObject):

    def __init__(self, driver):
        super().__init__(driver=driver)

    def verificar_tabela_amount_transaction_type(self, linha, valor_amount, transaction_type):
        verifica_valor_amount = self.driver.find_element(By.XPATH,
                                                         "//tbody/tr[" + linha + "]/td[2]").text == valor_amount
        verifica_transaction_type = self.driver.find_element(By.XPATH,
                                                             "//tbody/tr[" + linha + "]/td[3]").text == transaction_type

        return verifica_valor_amount and verifica_transaction_type

    def click_on_delete(self):
        self.driver.find_element(By.CSS_SELECTOR, "[ng-click='reset()']").click()

    def is_tabela_de_lista_de_transition_sem_registros(self):
        self.driver.implicitly_wait(2)
        try:
            self.driver.find_element(By.XPATH, "//tbody/tr")
        except:
            return True



