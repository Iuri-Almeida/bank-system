import uuid
from random import randint
from datetime import datetime
from typing import Self

from bank.bank_exception import BankException
from bank.transaction_type import TransactionType
from bank.transaction import Transaction


class BankAccount(object):
    def __init__(self, cpf: str, balance: float = 0) -> None:
        if balance < 0:
            raise ValueError("O saldo não pode ser negativo.")

        self.__cpf: str = cpf
        self.__balance: float = balance
        self.__agency: str = str(randint(1000, 9999))
        self.__account_number: str = str(randint(1000000, 9999999))
        self.__statement: list[Transaction] = []

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def agency(self) -> str:
        return self.__agency

    @property
    def account_number(self) -> str:
        return self.__account_number

    @property
    def statement(self) -> list[Transaction]:
        return self.__statement

    def deposit(self, value: float) -> None:
        self.__validate_value(value)

        self.__balance += value

        self.__add_to_statement(TransactionType.DEPOSIT, value, f"Depósito de R${value:.2f} na conta.", datetime.now())

    def withdraw(self, value: float) -> None:
        self.__validate_value(value)
        self.__validate_balance(value)

        self.__balance -= value

        self.__add_to_statement(TransactionType.WITHDRAW, value, f"Saque de R${value:.2f} da conta.", datetime.now())

    def transfer(self, to_account: Self, value: float) -> None:
        self.__validate_account(to_account)
        self.__validate_value(value)
        self.__validate_balance(value)

        self.__balance -= value

        to_account.__receive_transfer(self, value)

        self.__add_to_statement(TransactionType.TRANSFER, value, f"Transferência de R${value:.2f} para a conta {to_account.account_number}", datetime.now())

    def __receive_transfer(self, from_account: Self, value: float) -> None:
        self.__balance += value

        self.__add_to_statement(TransactionType.TRANSFER, value, f"Transferência de R${value:.2f} da conta {from_account.account_number}", datetime.now())

    def __add_to_statement(self, transaction_type: TransactionType, value: float, description: str, date: datetime) -> None:
        self.__statement.append(Transaction(str(uuid.uuid4()), transaction_type, value, description, date))

    def __validate_value(self, value: object) -> None:
        if value is None:
            raise BankException("Valor não pode ser vazio.")

        if not isinstance(value, (int, float)):
            raise TypeError("Valor precisa ser um número.")

        if not value:
            raise ValueError("Valor não pode ser zero.")

        if value < 0:
            raise ValueError("Valor não pode ser negativo.")

    def __validate_balance(self, value: float) -> None:
        if value > self.__balance:
            raise BankException("Saldo insuficiente. Operação não realizada.")

    def __validate_account(self, account: Self) -> None:
        if account == self:
            raise BankException("Não é possível transferir para a mesma conta.")

    def __str__(self) -> str:
        return f"CPF: {self.cpf}\nAgência: {self.agency}\nConta: {self.account_number}\nSaldo: R${self.balance:.2f}"

    def __repr__(self) -> str:
        return f"BankAccount('{self.cpf}', '{self.agency}', '{self.account_number}', {self.balance:.2f})"
