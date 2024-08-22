from os import system

from bank.bank_account import BankAccount
from application.ansi_color_constants import ANSIColorConstants


class UI(object):
    @staticmethod
    def clear_screen() -> None:
        system("cls")

    @staticmethod
    def show_menu() -> None:
        print(f"\n{ANSIColorConstants.ANSI_PURPLE}Banco do Iuri:{ANSIColorConstants.ANSI_RESET}")
        print(f"{ANSIColorConstants.ANSI_PURPLE}1 - {ANSIColorConstants.ANSI_YELLOW}Criar Conta (PF ou PJ){ANSIColorConstants.ANSI_RESET}")
        print(f"{ANSIColorConstants.ANSI_PURPLE}2 - {ANSIColorConstants.ANSI_YELLOW}Depositar{ANSIColorConstants.ANSI_RESET}")
        print(f"{ANSIColorConstants.ANSI_PURPLE}3 - {ANSIColorConstants.ANSI_YELLOW}Sacar{ANSIColorConstants.ANSI_RESET}")
        print(f"{ANSIColorConstants.ANSI_PURPLE}4 - {ANSIColorConstants.ANSI_YELLOW}Transferir{ANSIColorConstants.ANSI_RESET}")
        print(f"{ANSIColorConstants.ANSI_PURPLE}5 - {ANSIColorConstants.ANSI_YELLOW}Listar Contas{ANSIColorConstants.ANSI_RESET}")
        print(f"{ANSIColorConstants.ANSI_PURPLE}6 - {ANSIColorConstants.ANSI_YELLOW}Informações da Conta{ANSIColorConstants.ANSI_RESET}")
        print(f"{ANSIColorConstants.ANSI_PURPLE}7 - {ANSIColorConstants.ANSI_YELLOW}Extrato da Conta{ANSIColorConstants.ANSI_RESET}")
        print(f"{ANSIColorConstants.ANSI_PURPLE}8 - {ANSIColorConstants.ANSI_YELLOW}Excluir Conta{ANSIColorConstants.ANSI_RESET}")
        print(f"{ANSIColorConstants.ANSI_PURPLE}9 - {ANSIColorConstants.ANSI_YELLOW}Sair{ANSIColorConstants.ANSI_RESET}")

    @staticmethod
    def read_menu(msg: str) -> int:
        while True:
            try:
                choice = int(input(f"{ANSIColorConstants.ANSI_CYAN}{msg}{ANSIColorConstants.ANSI_RESET}").strip())
                if 1 <= choice <= 9:
                    return choice
                else:
                    print(f"{ANSIColorConstants.ANSI_RED}Opção inválida. Por favor, escolha uma opção entre 1 e 9.{ANSIColorConstants.ANSI_RESET}")
            except ValueError:
                print(f"{ANSIColorConstants.ANSI_RED}Opção inválida. Por favor, escolha uma opção entre 1 e 9.{ANSIColorConstants.ANSI_RESET}")

    @staticmethod
    def read_cpf_or_cnpj_value(msg: str) -> str:
        while True:
            value = input(f"{ANSIColorConstants.ANSI_GREEN}{msg}{ANSIColorConstants.ANSI_RESET}").strip()
            if (len(value) == 11 or len(value) == 14) and value.isdigit():
                return value
            else:
                print(f"{ANSIColorConstants.ANSI_RED}CPF/CNPJ inválido. Por favor, digite um CPF/CNPJ válido (11/14 dígitos).{ANSIColorConstants.ANSI_RESET}")

    @staticmethod
    def read_float_value(msg: str) -> float:
        while True:
            try:
                value = float(input(f"{ANSIColorConstants.ANSI_GREEN}{msg}{ANSIColorConstants.ANSI_RESET}").strip().replace(',', '.'))
                return value
            except ValueError:
                print(f"{ANSIColorConstants.ANSI_RED}Valor inválido. Por favor, digite um número.{ANSIColorConstants.ANSI_RESET}")

    @staticmethod
    def show_account_created(account: BankAccount) -> None:
        print(f"\n{ANSIColorConstants.ANSI_BLUE}Conta criada com sucesso!{ANSIColorConstants.ANSI_RESET}\n")
        print(account)

        input(f"\n{ANSIColorConstants.ANSI_PURPLE}Pressione ENTER para voltar ao menu.{ANSIColorConstants.ANSI_RESET}")

    @staticmethod
    def show_deposit_success(account: BankAccount, value: float) -> None:
        print(f"\n{ANSIColorConstants.ANSI_BLUE}Depósito realizado com sucesso!{ANSIColorConstants.ANSI_RESET}\n")
        print(f"CPF: {account.id}")
        print(f"Conta: {account.account_number}")
        print(f"Valor depositado: R${value:.2f}")
        print(f"Novo saldo: R${account.balance:.2f}")

        input(f"\n{ANSIColorConstants.ANSI_PURPLE}Pressione ENTER para voltar ao menu.{ANSIColorConstants.ANSI_RESET}")

    @staticmethod
    def show_withdraw_success(account: BankAccount, value: float) -> None:
        print(f"\n{ANSIColorConstants.ANSI_BLUE}Saque realizado com sucesso!{ANSIColorConstants.ANSI_RESET}\n")
        print(f"CPF: {account.id}")
        print(f"Conta: {account.account_number}")
        print(f"Valor sacado: R${value:.2f}")
        print(f"Novo saldo: R${account.balance:.2f}")
        print(f"Taxa: {account.tax:.2%}")

        input(f"\n{ANSIColorConstants.ANSI_PURPLE}Pressione ENTER para voltar ao menu.{ANSIColorConstants.ANSI_RESET}")

    @staticmethod
    def show_transfer_success(sender_account: BankAccount, receiver_account: BankAccount, value: float) -> None:
        print(f"\n{ANSIColorConstants.ANSI_BLUE}Transferência realizada com sucesso!{ANSIColorConstants.ANSI_RESET}")
        print(f"\nCPF de Origem: {sender_account.id}")
        print(f"Conta de Origem: {sender_account.account_number}")
        print(f"CPF de Destino: {receiver_account.id}")
        print(f"Conta de Destino: {receiver_account.account_number}")
        print(f"Valor transferido: R${value:.2f}")
        print(f"Taxa: {sender_account.tax:.2%}")
        print(f"Novo saldo na Conta de Origem: R${sender_account.balance:.2f}")
        print(f"Novo saldo na Conta de Destino: R${receiver_account.balance:.2f}")

        input(f"\n{ANSIColorConstants.ANSI_PURPLE}Pressione ENTER para voltar ao menu.{ANSIColorConstants.ANSI_RESET}")

    @staticmethod
    def show_accounts(accounts: dict[str, BankAccount]) -> None:
        for account in accounts.values():
            print(f"\n{ANSIColorConstants.ANSI_BLUE}============================{ANSIColorConstants.ANSI_RESET}\n")
            print(account)

        print(f"\n{ANSIColorConstants.ANSI_BLUE}============================{ANSIColorConstants.ANSI_RESET}")

        input(f"\n{ANSIColorConstants.ANSI_PURPLE}Pressione ENTER para voltar ao menu.{ANSIColorConstants.ANSI_RESET}")

    @staticmethod
    def show_account_info(account: BankAccount) -> None:
        print(f"\n{ANSIColorConstants.ANSI_BLUE}============================{ANSIColorConstants.ANSI_RESET}\n")
        print(account)
        print(f"\n{ANSIColorConstants.ANSI_BLUE}============================{ANSIColorConstants.ANSI_RESET}")

        input(f"\n{ANSIColorConstants.ANSI_PURPLE}Pressione ENTER para voltar ao menu.{ANSIColorConstants.ANSI_RESET}")

    @staticmethod
    def show_account_statement(account: BankAccount) -> None:
        print(f"\n{ANSIColorConstants.ANSI_BLUE}Extrato da Conta:{ANSIColorConstants.ANSI_RESET}")
        for transaction in account.statement:
            print(f"\n{ANSIColorConstants.ANSI_BLUE}============================{ANSIColorConstants.ANSI_RESET}\n")
            print(transaction)

        print(f"\n{ANSIColorConstants.ANSI_BLUE}============================{ANSIColorConstants.ANSI_RESET}")

        input(f"\n{ANSIColorConstants.ANSI_PURPLE}Pressione ENTER para voltar ao menu.{ANSIColorConstants.ANSI_RESET}")

    @staticmethod
    def show_account_deleted(account: BankAccount) -> None:
        print(f"\n{ANSIColorConstants.ANSI_BLUE}Conta excluída com sucesso!{ANSIColorConstants.ANSI_RESET}\n")
        print(account)

        input(f"\n{ANSIColorConstants.ANSI_PURPLE}Pressione ENTER para voltar ao menu.{ANSIColorConstants.ANSI_RESET}")

    @staticmethod
    def show_error_message(message: str) -> None:
        print(f"\n{ANSIColorConstants.ANSI_RED}{message}{ANSIColorConstants.ANSI_RESET}\n")

        input(f"{ANSIColorConstants.ANSI_PURPLE}Pressione ENTER para voltar ao menu.{ANSIColorConstants.ANSI_RESET}")

    @staticmethod
    def show_exit_message() -> None:
        print(f"\n{ANSIColorConstants.ANSI_GREEN}Saindo do sistema...{ANSIColorConstants.ANSI_RESET}\n")
        print(f"{ANSIColorConstants.ANSI_YELLOW}Obrigado por utilizar nosso sistema bancário!{ANSIColorConstants.ANSI_RESET}")
