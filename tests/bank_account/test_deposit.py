import pytest

from bank.bank_account import BankAccount
from bank.bank_exception import BankException
from bank.transaction_type import TransactionType


def test_deposit_value_100():
    account = BankAccount("12345678901")

    initial_balance = account.balance

    account.deposit(100)

    assert account.balance == initial_balance + 100
    assert len(account.statement) == 1
    assert account.statement[-1].transaction_type == TransactionType.DEPOSIT
    assert account.statement[-1].value == 100
    assert account.statement[-1].description == "Depósito de R$100.00 na conta."


def test_deposit_value_001():
    account = BankAccount("12345678901")

    initial_balance = account.balance

    account.deposit(0.01)

    assert account.balance == initial_balance + 0.01
    assert len(account.statement) == 1
    assert account.statement[-1].transaction_type == TransactionType.DEPOSIT
    assert account.statement[-1].value == 0.01
    assert account.statement[-1].description == "Depósito de R$0.01 na conta."


def test_deposit_none_value_should_raise_exception():
    account = BankAccount("12345678901")

    with pytest.raises(BankException) as e:
        account.deposit(None)

    assert str(e.value) == "Valor não pode ser vazio."


def test_deposit_zero_value_should_raise_exception():
    account = BankAccount("12345678901")

    with pytest.raises(ValueError) as e:
        account.deposit(0)

    assert str(e.value) == "Valor não pode ser zero."


def test_deposit_negative_value_should_raise_exception():
    bank_account = BankAccount("12345678901")

    value = -100.00

    with pytest.raises(ValueError) as exception_info:
        bank_account.deposit(value)

    assert str(exception_info.value) == "Valor não pode ser negativo."


def test_deposit_non_numeric_value_str():
    account = BankAccount("12345678901")

    with pytest.raises(TypeError) as e:
        account.deposit("abc")

    assert str(e.value) == "Valor precisa ser um número."


def test_deposit_list_value_should_raise_exception():
    account = BankAccount("12345678901")

    with pytest.raises(TypeError) as e:
        account.deposit([100.0])

    assert str(e.value) == "Valor precisa ser um número."


def test_deposit_non_numeric_value_should_raise_exception():
    account = BankAccount("12345678901")

    with pytest.raises(TypeError) as e:
        account.deposit({"key": "value"})

    assert str(e.value) == "Valor precisa ser um número."


def test_deposit_custom_object_should_raise_exception():
    account = BankAccount("12345678901")

    custom_object = object()

    with pytest.raises(TypeError) as e:
        account.deposit(custom_object)

    assert str(e.value) == "Valor precisa ser um número."


def test_deposit_positive_balance():
    account = BankAccount("12345678901", 100.0)

    value_to_deposit = 50.0

    account.deposit(value_to_deposit)

    assert account.balance == 150.0
    assert len(account.statement) == 1
    assert account.statement[-1].transaction_type == TransactionType.DEPOSIT
    assert account.statement[-1].value == value_to_deposit
    assert "Depósito de R$50.00 na conta." in account.statement[0].description


def test_deposit_multiple_transactions():
    account = BankAccount("12345678901")

    account.deposit(100.0)
    account.deposit(50.0)
    account.deposit(200.0)

    assert account.balance == 350.0
    assert len(account.statement) == 3
    assert account.statement[-1].transaction_type == TransactionType.DEPOSIT
    assert account.statement[-1].value == 200.0
    assert account.statement[-1].description == "Depósito de R$200.00 na conta."



