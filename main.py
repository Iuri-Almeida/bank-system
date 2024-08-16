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
                cpf = UI.read_cpf_value("\nQual o seu cpf? ")

                account = bank.create_account(cpf)

                UI.clear_screen()
                UI.show_account_created(account)

            elif choice == 2:
                cpf = UI.read_cpf_value("\nInforme o CPF da conta que deseja realizar o depósito: ")

                value = UI.read_float_value("\nQual valor deseja depositar? R$")

                bank.deposit(cpf, value)

                UI.clear_screen()
                UI.show_deposit_success(bank.get_account(cpf), value)

            elif choice == 3:
                cpf = UI.read_cpf_value("\nInforme o CPF da conta que deseja realizar o saque: ")

                value = UI.read_float_value("\nQual valor deseja sacar? R$")

                bank.withdraw(cpf, value)

                UI.clear_screen()
                UI.show_withdraw_success(bank.get_account(cpf), value)

            elif choice == 4:
                cpf_sender = UI.read_cpf_value("\nInforme o CPF da conta de origem: ")
                cpf_receiver = UI.read_cpf_value("\nInforme o CPF da conta de destino: ")

                value = UI.read_float_value("\nQual valor deseja transferir? R$")

                bank.transfer(cpf_sender, cpf_receiver, value)

                UI.clear_screen()
                UI.show_transfer_success(bank.get_account(cpf_sender), bank.get_account(cpf_receiver), value)

            elif choice == 5:
                UI.clear_screen()
                UI.show_accounts(bank.accounts)

            elif choice == 6:
                cpf = UI.read_cpf_value("\nInforme o CPF da conta que deseja ver os detalhes: ")

                UI.clear_screen()
                UI.show_account_info(bank.get_account(cpf))

            elif choice == 7:
                cpf = UI.read_cpf_value("\nInforme o CPF da conta que deseja ver o extrato: ")

                UI.clear_screen()
                UI.show_account_statement(bank.get_account(cpf))

            elif choice == 8:
                cpf = UI.read_cpf_value("\nInforme o CPF da conta que deseja excluir: ")

                UI.clear_screen()
                UI.show_account_deleted(bank.delete_account(cpf))

            else:
                break

        except BankException as e:
            print(e)
            input('\nClick ENTER to continue.')

    UI.clear_screen()
    print("Obrigado por utilizar nosso sistema. Até mais!")


if __name__ == "__main__":
    main()
