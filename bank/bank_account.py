from abc import ABC, abstractmethod
import uuid
from random import randint
from datetime import datetime
from typing import Self

from bank.bank_exception import BankException
from bank.transaction_type import TransactionType
from bank.transaction import Transaction


class BankAccount(ABC):
    def __init__(self, id: str, balance: float = 0) -> None:
        if balance < 0:
            raise ValueError("O saldo não pode ser negativo.")

        self.__id: str = id
        self._balance: float = balance
        self.__agency: str = str(randint(1000, 9999))
        self.__account_number: str = str(randint(1000000, 9999999))
        self.__statement: list[Transaction] = []
        self.__tax = 0

    @property
    def id(self) -> str:
        return self.__id

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def agency(self) -> str:
        return self.__agency

    @property
    def account_number(self) -> str:
        return self.__account_number

    @property
    def statement(self) -> list[Transaction]:
        return self.__statement

    @property
    def tax(self) -> float:
        return self.__tax

    def deposit(self, value: float) -> None:
        self._validate_value(value)

        self._balance += value

        self._add_to_statement(TransactionType.DEPOSIT, value, f"Depósito de R${value:.2f} na conta.", datetime.now())

    @abstractmethod
    def withdraw(self, value: float) -> None:
        pass

    @abstractmethod
    def transfer(self, to_account: Self, value: float) -> None:
        pass

    def _receive_transfer(self, from_account: Self, value: float) -> None:
        self._balance += value

        self._add_to_statement(TransactionType.TRANSFER, value, f"Transferência de R${value:.2f} da conta {from_account.account_number}", datetime.now())

    def _add_to_statement(self, transaction_type: TransactionType, value: float, description: str, date: datetime) -> None:
        self.__statement.append(Transaction(str(uuid.uuid4()), transaction_type, value, description, date))

    def _validate_value(self, value: object) -> None:
        if value is None:
            raise BankException("Valor não pode ser vazio.")

        if not isinstance(value, (int, float)):
            raise TypeError("Valor precisa ser um número.")

        if not value:
            raise ValueError("Valor não pode ser zero.")

        if value < 0:
            raise ValueError("Valor não pode ser negativo.")

    def _validate_balance(self, value: float) -> None:
        if value > self._balance:
            raise BankException("Saldo insuficiente. Operação não realizada.")

    def _validate_account(self, account: Self) -> None:
        if account == self:
            raise BankException("Não é possível transferir para a mesma conta.")
