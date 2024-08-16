from bank.bank_account import BankAccount
from bank.bank_exception import BankException


class Bank(object):
    def __init__(self) -> None:
        self.__accounts: dict[str, BankAccount] = {}

        self.__initial_setup()

    @property
    def accounts(self) -> dict[str, BankAccount]:
        return self.__accounts

    def create_account(self, id: str) -> BankAccount:
        self.__validate_cpf(id)

        if id in self.__accounts:
            raise BankException(f"Conta já cadastrada para o CPF/CNPJ {id}.")

        new_account = BankAccount(id)

        self.__accounts[id] = new_account

        return new_account

    def get_account(self, id: str) -> BankAccount:
        self.__validate_cpf(id)

        if id in self.__accounts:
            return self.__accounts[id]

        raise BankException(f"Conta não encontrada para o CPF/CNPJ {id}.")

    def delete_account(self, id: str) -> BankAccount:
        self.__validate_cpf(id)

        if id in self.__accounts:
            if self.get_account(id).balance == 0:
                return self.__accounts.pop(id)

            raise BankException(f"Não é possível excluir a conta {id} com saldo não zero.")

        raise BankException(f"Conta não encontrada para o CPF/CNPJ {id}.")

    def deposit(self, id: str, value: float) -> None:
        account = self.get_account(id)
        account.deposit(value)

    def withdraw(self, id: str, value: float) -> None:
        account = self.get_account(id)
        account.withdraw(value)

    def transfer(self, from_id: str, to_id: str, value: float) -> None:
        sender_account = self.get_account(from_id)
        receiver_account = self.get_account(to_id)

        sender_account.transfer(receiver_account, value)

    def __validate_id(self, id: object, obj: str) -> None:
        if not id or id is None:
            raise BankException(f"{obj} não pode estar vazio.")

        if not isinstance(id, str):
            raise TypeError(f"{obj} deve ser uma string.")

        if not id.isdigit():
            raise ValueError(f"{obj} deve conter apenas dígitos.")

    def __validate_cpf(self, cpf: str) -> None:
        self.__validate_id(cpf, "CPF")

        if len(cpf) != 11:
            raise ValueError("CPF deve ter 11 dígitos.")

    def __initial_setup(self):
        self.create_account("00000000000")

    def __str__(self) -> str:
        return str(self.accounts)

    def __repr__(self) -> str:
        return f"Bank({self.__str__()})"
