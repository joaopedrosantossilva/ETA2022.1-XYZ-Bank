from faker import Faker
from pages.AccountPage import AccountPage
from pages.AddCustomerPage import AddCustomerPage
from pages.BankManagerPage import BankManagerPage
from pages.CustomerLoginPage import CustomerLoginPage
from pages.DepositPage import DepositPage
from pages.ListCustomersPage import ListCustomersPage
from pages.OpenAccountPage import OpenAccountPage


class Test1:
    def test_criar_customer(self, open_home):
        #Generation Data
        generator = Faker()
        first_name = generator.unique.first_name()
        last_name = generator.unique.last_name()
        post_code = generator.postcode()
        open_home.click_on_bank_manager_login()
        bank_manager_page = BankManagerPage(open_home.driver)
        assert bank_manager_page.is_url_page(), "A url está diferente do esperado"
        bank_manager_page.clicar_em_add_customer()
        add_customer_page = AddCustomerPage(bank_manager_page.driver)
        assert add_customer_page.is_form_displayed(), "O formulário não foi exibido"
        add_customer_page.set_form_and_click_on_add_customer(first_name,last_name,post_code)
        assert add_customer_page.msg_customer_added_sucessfully_displayed(), "O alerta não foi exibido ou o texto exibido no alerta está diferente do esperado"
        add_customer_page.accept_alert()

    def test_logar_com_usuario_que_nao_tem_uma_conta_associada(self, create_customer):
        home_page = create_customer[0]
        home_page.open_home_page()
        home_page.click_on_customer_login()
        user = ""+create_customer[1]+" "+create_customer[2]
        customer_login_page = CustomerLoginPage(create_customer[0].driver)
        customer_login_page.select_user(user)
        customer_login_page.click_on_login()
        account_page = AccountPage(customer_login_page.driver)
        assert account_page.is_msg_welcome_user_displayed(user), "Nome do usuário diferente do esperado"
        assert account_page.is_msg_please_open_an_account_displayed(), "Mensagem diferente do esperado"

    def test_criar_conta_para_usuario_com_currency_dollar(self,create_customer):
        home_page = create_customer[0]
        user = "" + create_customer[1] + " " + create_customer[2]
        home_page.open_home_page()
        home_page.click_on_bank_manager_login()
        bank_manager_page = BankManagerPage(home_page.driver)
        assert bank_manager_page.is_url_page(), "A url está diferente do esperado"
        bank_manager_page.click_on_open_account()
        open_account_page = OpenAccountPage(bank_manager_page.driver)
        open_account_page.select_customer(user)
        open_account_page.select_currency("Dollar")
        open_account_page.click_on_process()
        assert open_account_page.msg_account_created_sucessfully_displayed(), "O alerta não foi exibido ou o texto exibido no alerta está diferente do esperado"
    def test_delete_customers(self, create_customer):
        home_page = create_customer[0]
        first_name = create_customer[1]
        home_page.click_on_customers()
        list_customers_page = ListCustomersPage(home_page.driver)
        list_customers_page.is_table_with_list_of_customers_displayed(), "Tabela não foi exibida"
        list_customers_page.search_customer(first_name)
        list_customers_page.click_on_delete()
        list_customers_page.clear_search_customer()
        assert list_customers_page.the_name_is_no_longer_on_the_customer_list(first_name), "O nome continua presente na lista"

    def test_realizar_deposito(self, create_account_with_dollar):
        value_balance_inicial = '0'
        new_value_balance = '300'
        home_page = create_account_with_dollar[0]
        user = create_account_with_dollar[1]
        home_page.open_home_page()
        home_page.click_on_customer_login()
        customer_login_page = CustomerLoginPage(home_page.driver)
        customer_login_page.select_user(user)
        customer_login_page.click_on_login()
        account_page = AccountPage(customer_login_page.driver)
        assert account_page.is_msg_welcome_user_displayed(user), "Nome do usuário diferente do esperado"
        assert account_page.is_value_balance(value_balance_inicial), "Valor diferente do esperado"
        account_page.click_on_deposit()
        deposit_page = DepositPage(account_page.driver)
        deposit_page.amount_to_be_deposited(new_value_balance)
        deposit_page.click_on_deposit()
        assert deposit_page.validated_message_deposit_success(), "Depósito não efetuado ou mensgem incorreta"
        assert account_page.is_value_balance(new_value_balance), "Valor diferente do esperado"

