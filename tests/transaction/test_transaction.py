from datetime import datetime

from bank.transaction import Transaction
from bank.transaction_type import TransactionType


def test_transaction_str_representation_deposit():
    transaction_id = "T123"
    transaction_type = TransactionType.DEPOSIT
    value = 100.50
    description = "Teste depósito"
    date = datetime(2022, 1, 1, 10, 0, 0)

    transaction = Transaction(transaction_id, transaction_type, value, description, date)

    result = str(transaction)

    expected_result = "Número da Transação: T123\nTipo: Depósito\nValor: R$100.50\nDescrição: Teste depósito\nData: 2022-01-01 10:00:00"

    assert result == expected_result


def test_transaction_str_representation_withdraw():
    transaction_id = "T123"
    transaction_type = TransactionType.WITHDRAW
    value = 100.50
    description = "Teste depósito"
    date = datetime(2022, 1, 1, 10, 0, 0)

    transaction = Transaction(transaction_id, transaction_type, value, description, date)

    result = str(transaction)

    expected_result = "Número da Transação: T123\nTipo: Saque\nValor: R$100.50\nDescrição: Teste depósito\nData: 2022-01-01 10:00:00"

    assert result == expected_result


def test_transaction_str_representation_transfer():
    transaction_id = "T123"
    transaction_type = TransactionType.TRANSFER
    value = 100.50
    description = "Teste depósito"
    date = datetime(2022, 1, 1, 10, 0, 0)

    transaction = Transaction(transaction_id, transaction_type, value, description, date)

    result = str(transaction)

    expected_result = "Número da Transação: T123\nTipo: Transferência\nValor: R$100.50\nDescrição: Teste depósito\nData: 2022-01-01 10:00:00"

    assert result == expected_result


def test_transaction_repr_representation():
    transaction_id = "T123"
    transaction_type = TransactionType.DEPOSIT
    value = 100.50
    description = "Teste depósito"
    date = datetime(2022, 1, 1, 10, 0, 0)

    transaction = Transaction(transaction_id, transaction_type, value, description, date)

    result = repr(transaction)

    expected_result = f"Transaction('T123', 'TransactionType.DEPOSIT', 100.50, 'Teste depósito', '2022-01-01 10:00:00'"

    assert result == expected_result
