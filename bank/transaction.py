from datetime import datetime

from bank.transaction_type import TransactionType


class Transaction(object):
    def __init__(self, transaction_id: str, transaction_type: TransactionType, value: float, description: str, date: datetime):
        self.__transaction_id: str = transaction_id
        self.__transaction_type: TransactionType = transaction_type
        self.__value: float = value
        self.__description: str = description
        self.__date: datetime = date

    @property
    def transaction_id(self) -> str:
        return self.__transaction_id

    @property
    def transaction_type(self) -> TransactionType:
        return self.__transaction_type

    @property
    def value(self) -> float:
        return self.__value

    @property
    def description(self) -> str:
        return self.__description

    @property
    def date(self) -> datetime:
        return self.__date

    def __transaction_type_to_str(self) -> str:
        if self.__transaction_type == TransactionType.DEPOSIT:
            return "Depósito"
        elif self.__transaction_type == TransactionType.WITHDRAW:
            return "Saque"
        elif self.__transaction_type == TransactionType.TRANSFER:
            return "Transferência"

    def __str__(self) -> str:
        return f"Número da Transação: {self.transaction_id}\nTipo: {self.__transaction_type_to_str()}\nValor: R${self.value:.2f}\nDescrição: {self.description}\nData: {self.date}"

    def __repr__(self) -> str:
        return f"Transaction('{self.transaction_id}', '{self.transaction_type}', {self.value:.2f}, '{self.description}', '{self.date}'"
