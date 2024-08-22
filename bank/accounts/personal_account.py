from abc import ABC
from datetime import datetime

from bank.bank_account import BankAccount
from bank.transaction_type import TransactionType


class PersonalAccount(BankAccount, ABC):
    def __init__(self, cpf: str, balance: float = 0) -> None:
        super().__init__(cpf, balance)

    def withdraw(self, value: float) -> None:
        self._validate_value(value)
        self._validate_balance(value)

        self._balance -= value

        self._add_to_statement(TransactionType.WITHDRAW, value, f"Saque de R${value:.2f} da conta.", datetime.now())

    def transfer(self, to_account: BankAccount, value: float) -> None:
        self._validate_account(to_account)
        self._validate_value(value)
        self._validate_balance(value)

        self._balance -= value

        to_account._receive_transfer(self, value)

        self._add_to_statement(TransactionType.TRANSFER, value, f"Transferência de R${value:.2f} para a conta {to_account.account_number}", datetime.now())

    def __str__(self) -> str:
        return f"CPF: {self.id}\nAgência: {self.agency}\nConta: {self.account_number}\nSaldo: R${self.balance:.2f}"

    def __repr__(self) -> str:
        return f"PersonalAccount('{self.id}', '{self.agency}', '{self.account_number}', {self.balance:.2f})"
