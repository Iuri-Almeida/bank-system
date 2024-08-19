from application.ui import UI
from bank.bank import Bank
from bank.bank_exception import BankException


def main():

    bank = Bank()

    while True:
        try:
            UI.clear_screen()

            UI.show_menu()
            choice = UI.read_menu("\nEscolha: ")

            if choice == 1:
                id = UI.read_cpf_or_cnpj_value("\nQual o seu CPF/CNPJ? ")

                account = bank.create_account(id)

                UI.clear_screen()
                UI.show_account_created(account)

            elif choice == 2:
                id = UI.read_cpf_or_cnpj_value("\nInforme o CPF/CNPJ da conta que deseja realizar o depósito: ")

                account = bank.get_account(id)

                value = UI.read_float_value("\nQual valor deseja depositar? R$")

                bank.deposit(account, value)

                UI.clear_screen()
                UI.show_deposit_success(account, value)

            elif choice == 3:
                id = UI.read_cpf_or_cnpj_value("\nInforme o CPF/CNPJ da conta que deseja realizar o saque: ")

                account = bank.get_account(id)

                value = UI.read_float_value("\nQual valor deseja sacar? R$")

                bank.withdraw(account, value)

                UI.clear_screen()
                UI.show_withdraw_success(account, value)

            elif choice == 4:
                id_sender = UI.read_cpf_or_cnpj_value("\nInforme o CPF/CNPJ da conta de origem: ")
                sender_account = bank.get_account(id_sender)

                id_receiver = UI.read_cpf_or_cnpj_value("\nInforme o CPF/CNPJ da conta de destino: ")
                receiver_account = bank.get_account(id_receiver)

                value = UI.read_float_value("\nQual valor deseja transferir? R$")

                bank.transfer(sender_account, receiver_account, value)

                UI.clear_screen()
                UI.show_transfer_success(sender_account, receiver_account, value)

            elif choice == 5:
                UI.clear_screen()
                UI.show_accounts(bank.accounts)

            elif choice == 6:
                id = UI.read_cpf_or_cnpj_value("\nInforme o CPF/CNPJ da conta que deseja ver os detalhes: ")

                account = bank.get_account(id)

                UI.clear_screen()
                UI.show_account_info(account)

            elif choice == 7:
                id = UI.read_cpf_or_cnpj_value("\nInforme o CPF/CNPJ da conta que deseja ver o extrato: ")

                account = bank.get_account(id)

                UI.clear_screen()
                UI.show_account_statement(account)

            elif choice == 8:
                id = UI.read_cpf_or_cnpj_value("\nInforme o CPF/CNPJ da conta que deseja excluir: ")

                UI.clear_screen()
                UI.show_account_deleted(bank.delete_account(id))

            else:
                break

        except (BankException, ValueError) as e:
            print(e)
            input('\nClick ENTER to continue.')

    UI.clear_screen()
    print("Obrigado por utilizar nosso sistema. Até mais!")


if __name__ == "__main__":
    main()
