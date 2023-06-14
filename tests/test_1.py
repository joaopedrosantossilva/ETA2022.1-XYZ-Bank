import time
from faker import Faker
from pages.AddCustomerPage import AddCustomerPage
from pages.BankManagerPage import BankManagerPage
from pages.CustomerLoginPage import CustomerLoginPage
from pages.OpenAccountPage import OpenAccountPage


class Test1:
    def test_criar_customer(self, open_home):
        #Generation Data
        generator = Faker()
        first_name = generator.unique.first_name()
        last_name = generator.unique.last_name()
        post_code = generator.postcode()
        open_home.clicar_em_bank_manager_login()
        bank_manager_page = BankManagerPage(open_home.driver)
        bank_manager_page.clicar_em_add_customer()
        add_customer_page = AddCustomerPage(bank_manager_page.driver)
        assert add_customer_page.is_form_displayed(), "O formulário não foi exibido"
        add_customer_page.set_form_and_click_on_add_customer(first_name,last_name,post_code)
        assert add_customer_page.msg_customer_added_sucessfully_displayed(), "O alerta não foi exibido ou o texto exibido no alerta está diferente do esperado"
        add_customer_page.accept_alert()

    def test_logar_com_usuario_que_nao_tem_uma_conta_associada(self, create_customer):
        create_customer[0].clicar_customer_login()
        customer_login_page = CustomerLoginPage(create_customer[0].driver)
        customer_login_page.select_user("Customer Sem Account Teste")
        customer_login_page.click_on_login()
        time.sleep(5)

    def test_criar_conta_para_usuario_com_currency_dollar(self,open_home):
        open_home.clicar_em_bank_manager_login()
        bank_manager_page = BankManagerPage(open_home.driver)
        bank_manager_page.click_on_open_account()
        open_account_page = OpenAccountPage(bank_manager_page.driver)
        open_account_page.select_customer("Ron Weasly")
        open_account_page.select_currency("Dollar")
        open_account_page.click_on_process()
        assert open_account_page.msg_account_created_sucessfully_displayed(), "O alerta não foi exibido ou o texto exibido no alerta está diferente do esperado"

