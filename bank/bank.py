from bank.bank_account import BankAccount
from bank.bank_exception import BankException


class Bank(object):
    def __init__(self):
        self.__accounts: dict[str, BankAccount] = {}

    @property
    def accounts(self) -> dict[str, BankAccount]:
        return self.__accounts

    def create_account(self, cpf: str) -> BankAccount:
        self.__validate_cpf(cpf)

        if cpf in self.__accounts:
            raise BankException(f"Conta já cadastrada para o CPF {cpf}.")

        new_account = BankAccount(cpf)

        self.__accounts[cpf] = new_account

        return new_account

    def get_account(self, cpf: str) -> BankAccount:
        self.__validate_cpf(cpf)

        if cpf in self.__accounts:
            return self.__accounts[cpf]

        raise BankException(f"Conta não encontrada para o CPF {cpf}.")

    def delete_account(self, cpf: str) -> BankAccount:
        self.__validate_cpf(cpf)

        if cpf in self.__accounts:
            if self.get_account(cpf).balance == 0:
                return self.__accounts.pop(cpf)

            raise BankException(f"Não é possível excluir a conta {cpf} com saldo não zero.")

        raise BankException(f"Conta não encontrada para o CPF {cpf}.")

    def deposit(self, cpf: str, value: float) -> None:
        account = self.get_account(cpf)
        account.deposit(value)

    def withdraw(self, cpf: str, value: float) -> None:
        account = self.get_account(cpf)
        account.withdraw(value)

    def transfer(self, from_cpf: str, to_cpf: str, value: float) -> None:
        sender_account = self.get_account(from_cpf)
        receiver_account = self.get_account(to_cpf)

        sender_account.transfer(receiver_account, value)

    def __validate_cpf(self, cpf) -> None:
        if not cpf or cpf is None:
            raise BankException("CPF não pode estar vazio.")

        if not isinstance(cpf, str):
            raise TypeError("CPF deve ser uma string.")

        if len(cpf) != 11:
            raise ValueError("CPF deve ter 11 dígitos.")

        if not cpf.isdigit():
            raise ValueError("CPF deve conter apenas dígitos.")

    def __str__(self) -> str:
        return str(self.accounts)

    def __repr__(self) -> str:
        return f"Bank({self.__str__()})"
