from bank.bank_account import BankAccount
from bank.bank_exception import BankException
from bank.accounts.personal_account import PersonalAccount
from bank.accounts.legal_entity_account import LegalEntityAccount


class Bank(object):
    def __init__(self) -> None:
        self.__accounts: dict[str, BankAccount] = {}

        self.__initial_setup()

    @property
    def accounts(self) -> dict[str, BankAccount]:
        return self.__accounts

    def create_account(self, id: str) -> BankAccount:
        is_cpf = self.__validate_cpf(id)
        is_cnpj = self.__validate_cnpj(id)

        if not is_cpf and not is_cnpj:
            raise ValueError(f"CPF/CNPJ inválido para o valor '{id}'. CPF deve ter 11 dígitos e CNPJ deve ter 14 dígitos.")

        if id in self.__accounts:
            raise BankException(f"Conta já cadastrada para o CPF/CNPJ {id}.")

        new_account = PersonalAccount(id) if is_cpf else LegalEntityAccount(id)

        self.__accounts[id] = new_account

        return new_account

    def get_account(self, id: str) -> BankAccount:
        if id in self.__accounts:
            return self.__accounts[id]

        raise ValueError(f"Conta não encontrada para o CPF/CNPJ {id}.")

    def delete_account(self, id: str) -> BankAccount:
        if id in self.__accounts:
            if self.get_account(id).balance == 0:
                return self.__accounts.pop(id)

            raise BankException(f"Não é possível excluir a conta {id} com saldo não zero.")

        raise ValueError(f"Conta não encontrada para o CPF/CNPJ {id}.")

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

    def __validate_id(self, id: object) -> None:
        if not id or id is None:
            raise BankException(f"CPF/CNPJ não pode estar vazio.")

        if not isinstance(id, str):
            raise TypeError(f"CPF/CNPJ deve ser uma string.")

        if not id.isdigit():
            raise ValueError(f"CPF/CNPJ deve conter apenas dígitos.")

    def __validate_cpf(self, cpf: str) -> bool:
        self.__validate_id(cpf)

        return len(cpf) == 11

    def __validate_cnpj(self, cnpj: str) -> bool:
        self.__validate_id(cnpj)

        return len(cnpj) == 14

    def __initial_setup(self):
        root_account = PersonalAccount("00000000000", 9999999999)
        self.__accounts["00000000000"] = root_account

    def __str__(self) -> str:
        return str(self.accounts)

    def __repr__(self) -> str:
        return f"Bank({self.__str__()})"
