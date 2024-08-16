from os import system

from bank.bank_account import BankAccount


class UI(object):
    @staticmethod
    def clear_screen() -> None:
        system("cls")

    @staticmethod
    def show_menu() -> None:
        print("\nBanco do Iuri:")
        print("1 - Criar Conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Transferir")
        print("5 - Listar Contas")
        print("6 - Informações da Conta")
        print("7 - Extrato da Conta")
        print("8 - Excluir Conta")
        print("9 - Sair")

    @staticmethod
    def read_menu(msg: str) -> int:
        while True:
            try:
                choice = int(input(msg))
                if 1 <= choice <= 9:
                    return choice
                else:
                    print("Opção inválida. Por favor, escolha uma opção entre 1 e 9.")
            except ValueError:
                print("Opção inválida. Por favor, escolha uma opção entre 1 e 9.")

    @staticmethod
    def read_cpf_value(msg: str) -> str:
        while True:
            value = input(msg)
            if len(value) == 11 and value.isdigit():
                return value
            else:
                print("CPF inválido. Por favor, digite um CPF válido (11 dígitos).")

    @staticmethod
    def read_float_value(msg: str) -> float:
        while True:
            try:
                value = float(input(msg).replace(',', '.'))
                return value
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")

    @staticmethod
    def read_yes_or_no_answer(msg: str) -> str:
        while True:
            try:
                answer = input(msg).lower()[0]
                if answer == "s" or answer == "n":
                    return answer
                else:
                    print("Resposta inválida. Por favor, responda 's' ou 'n'.")
            except IndexError:
                print("Resposta inválida. Por favor, responda 's' ou 'n'.")

    @staticmethod
    def show_account_created(account: BankAccount) -> None:
        print(f"\nConta criada com sucesso!\n")
        print(account)

        input("\nPressione ENTER para voltar ao menu.")

    @staticmethod
    def show_deposit_success(account: BankAccount, value: float) -> None:
        print(f"\nDepósito realizado com sucesso!\n")
        print(f"CPF: {account.id}")
        print(f"Conta: {account.account_number}")
        print(f"Valor depositado: R${value:.2f}")
        print(f"Novo saldo: R${account.balance:.2f}")

        input("\nPressione ENTER para voltar ao menu.")

    @staticmethod
    def show_withdraw_success(account: BankAccount, value: float) -> None:
        print(f"\nSaque realizado com sucesso!\n")
        print(f"CPF: {account.id}")
        print(f"Conta: {account.account_number}")
        print(f"Valor sacado: R${value:.2f}")
        print(f"Novo saldo: R${account.balance:.2f}")

        input("\nPressione ENTER para voltar ao menu.")

    @staticmethod
    def show_transfer_success(sender_account: BankAccount, receiver_account: BankAccount, value: float) -> None:
        print(f"\nTransferência realizada com sucesso!")
        print(f"\nCPF de Origem: {sender_account.id}")
        print(f"Conta de Origem: {sender_account.account_number}")
        print(f"CPF de Destino: {receiver_account.id}")
        print(f"Conta de Destino: {receiver_account.account_number}")
        print(f"Valor transferido: R${value:.2f}")
        print(f"Novo saldo na Conta de Origem: R${sender_account.balance:.2f}")
        print(f"Novo saldo na Conta de Destino: R${receiver_account.balance:.2f}")

        input("\nPressione ENTER para voltar ao menu.")

    @staticmethod
    def show_accounts(accounts: dict[str, BankAccount]) -> None:
        for account in accounts.values():
            print("\n============================\n")
            print(account)

        print("\n============================")

        input("\nPressione ENTER para voltar ao menu.")

    @staticmethod
    def show_account_info(account: BankAccount) -> None:
        print("\n============================\n")
        print(account)
        print("\n============================")

        input("\nPressione ENTER para voltar ao menu.")

    @staticmethod
    def show_account_statement(account: BankAccount) -> None:
        print("\nExtrato da Conta:")
        for transaction in account.statement:
            print("\n============================\n")
            print(transaction)

        print("\n============================")

        input("\nPressione ENTER para voltar ao menu.")

    @staticmethod
    def show_account_deleted(account: BankAccount) -> None:
        print(f"\nConta excluída com sucesso!\n")
        print(account)

        input("\nPressione ENTER para voltar ao menu.")
