from faker import Faker
from pages.AccountPage import AccountPage
from pages.AddCustomerPage import AddCustomerPage
from pages.BankManagerPage import BankManagerPage
from pages.CustomerLoginPage import CustomerLoginPage
from pages.DepositPage import DepositPage
from pages.ListCustomersPage import ListCustomersPage
from pages.OpenAccountPage import OpenAccountPage
from pages.TransactionsPage import TransactionsPage
from pages.WithdrawlPage import WithdrawlPage
import time


class Test1:
    def test_create_customer(self, open_home):
        # Generation Data
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
        add_customer_page.set_form_and_click_on_add_customer(first_name, last_name, post_code)
        assert add_customer_page.msg_customer_added_sucessfully_displayed(), "O alerta não foi exibido ou o texto exibido no alerta está diferente do esperado"
        add_customer_page.accept_alert()

    def test_login_with_the_user_who_does_not_have_an_associated_account(self, create_customer):
        home_page = create_customer[0]
        home_page.open_home_page()
        home_page.click_on_customer_login()
        user = "" + create_customer[1] + " " + create_customer[2]
        customer_login_page = CustomerLoginPage(create_customer[0].driver)
        customer_login_page.select_user(user)
        customer_login_page.click_on_login()
        account_page = AccountPage(customer_login_page.driver)
        assert account_page.is_msg_welcome_user_displayed(user), "Nome do usuário diferente do esperado"
        assert account_page.is_msg_please_open_an_account_displayed(), "Mensagem diferente do esperado"

    def test_create_an_account_for_the_user_with_currency_dollar(self, create_customer):
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
        assert open_account_page.msg_account_created_successfully_displayed(), "O alerta não foi exibido ou o texto exibido no alerta está diferente do esperado"

    def test_delete_customers(self, create_customer):
        home_page = create_customer[0]
        first_name = create_customer[1]
        home_page.open_home_page()
        home_page.click_on_bank_manager_login()
        bank_manager_page = BankManagerPage(home_page.driver)
        bank_manager_page.click_on_customers()
        list_customers_page = ListCustomersPage(home_page.driver)
        list_customers_page.is_table_with_list_of_customers_displayed(), "Tabela não foi exibida"
        list_customers_page.search_customer(first_name)
        list_customers_page.click_on_delete()
        list_customers_page.clear_search_customer()
        assert list_customers_page.the_name_is_no_longer_on_the_customer_list(
            first_name), "O nome continua presente na lista"

    def test_make_deposit(self, create_an_account_with_dollar_and_login):
        value_balance_inicial = '0'
        new_value_balance = '300'
        account_page = AccountPage(create_an_account_with_dollar_and_login.driver)
        assert account_page.is_value_balance(value_balance_inicial), "Valor diferente do esperado"
        account_page.click_on_deposit()
        deposit_page = DepositPage(account_page.driver)
        deposit_page.amount_to_be_deposited(new_value_balance)
        deposit_page.click_on_deposit()
        assert deposit_page.validated_message_deposit_success(), "Depósito não efetuado ou mensagem incorreta"
        assert account_page.is_value_balance(new_value_balance), "Valor diferente do esperado"

    def test_try_to_withdraw_an_amount_greater_than_the_current_balance(self, create_an_account_with_dollar_and_login):
        value_balance_inicial = '0'
        value_debit = '40'
        account_page = AccountPage(create_an_account_with_dollar_and_login.driver)
        assert account_page.is_value_balance(value_balance_inicial), "Valor diferente do esperado"
        account_page.click_on_withdrawl()
        withdrawl_page = WithdrawlPage(account_page.driver)
        withdrawl_page.set_amount(value_debit)
        withdrawl_page.send_withdrawl()
        assert withdrawl_page.is_msg_transaction_failed_displayed(), "Não foi exibido a mensagem ou a mensagem exibida é diferente do esperado."

    def test_make_withdraw(self, create_an_account_with_dollar_and_login):
        value_balance_inicial = '0'
        value_deposited = '300'
        value_debit = '200'
        value_balance_final = '100'
        account_page = AccountPage(create_an_account_with_dollar_and_login.driver)
        assert account_page.is_value_balance(value_balance_inicial), "Valor diferente do esperado"
        account_page.click_on_deposit()
        deposit_page = DepositPage(account_page.driver)
        deposit_page.amount_to_be_deposited(value_deposited)
        deposit_page.click_on_deposit()
        assert deposit_page.validated_message_deposit_success(), "Depósito não efetuado ou mensagem incorreta"
        assert account_page.is_value_balance(value_deposited), "Valor diferente do esperado"
        account_page.click_on_withdrawl()
        withdrawl_page = WithdrawlPage(account_page.driver)
        assert withdrawl_page.validated_tela_withdrawl(), "Tela incorreta"
        withdrawl_page.set_amount(value_debit)
        withdrawl_page.send_withdrawl()
        assert withdrawl_page.is_msg_transaction_success_displayed(), "Mensagem de sucesso na transação, não exibida!"
        assert account_page.is_value_balance(value_balance_final), "Valor balance final diferente do esperado"

    def test_validate_transaction_history(self, create_an_account_with_dollar_and_login):
        value_deposito = '300'
        value_saque = '100'
        account_page = AccountPage(create_an_account_with_dollar_and_login.driver)
        account_page.click_on_deposit()
        deposit_page = DepositPage(account_page.driver)
        deposit_page.amount_to_be_deposited(value_deposito)
        deposit_page.click_on_deposit()
        assert deposit_page.validated_message_deposit_success(), "Depósito não efetuado ou mensagem incorreta"
        account_page.click_on_withdrawl()
        withdrawl_page = WithdrawlPage(account_page.driver)
        assert withdrawl_page.validated_tela_withdrawl(), "Tela incorreta"
        withdrawl_page.set_amount(value_saque)
        withdrawl_page.send_withdrawl()
        assert withdrawl_page.is_msg_transaction_success_displayed(), "Mensagem de sucesso na transação não exibida!"
        time.sleep(2)
        account_page.click_on_transactions()
        transactions_page = TransactionsPage(withdrawl_page.driver)
        assert transactions_page.verificar_tabela_amount_transaction_type("1", ""+value_deposito+"", "Credit")
        assert transactions_page.verificar_tabela_amount_transaction_type("2", ""+value_saque+"", "Debit")

    def test_reset_transaction(self, create_an_account_with_dollar_and_login):
        value_deposito = '300'
        account_page = AccountPage(create_an_account_with_dollar_and_login.driver)
        account_page.click_on_deposit()
        deposit_page = DepositPage(account_page.driver)
        deposit_page.amount_to_be_deposited(value_deposito)
        deposit_page.click_on_deposit()
        assert deposit_page.validated_message_deposit_success(), "Depósito não efetuado ou mensagem incorreta"
        time.sleep(2)
        account_page.click_on_transactions()
        transactions_page = TransactionsPage(deposit_page.driver)
        assert transactions_page.verificar_tabela_amount_transaction_type("1", "300", "Credit"), "Valores diferentes do esperado"
        transactions_page.click_on_delete()
        assert transactions_page.is_tabela_de_lista_de_transition_sem_registros(), "Ainda possui registros na tabela."


