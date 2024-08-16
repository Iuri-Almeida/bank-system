import pytest

from bank.bank_account import BankAccount
from bank.bank_exception import BankException
from bank.transaction_type import TransactionType


def test_withdraw_negative_value():
    bank_account = BankAccount("12345678901")

    bank_account.deposit(100)

    with pytest.raises(ValueError) as e:
        bank_account.withdraw(-10)
    
    assert str(e.value) == "Valor não pode ser negativo."


def test_withdraw_none_value():
    account = BankAccount("12345678901")
    account.deposit(100.0)

    with pytest.raises(BankException) as e:
        account.withdraw(None)

    assert str(e.value) == "Valor não pode ser vazio."


def test_withdraw_zero_value():
    account = BankAccount("12345678901")
    account.deposit(100.0)

    with pytest.raises(ValueError) as e:
        account.withdraw(0)

    assert str(e.value) == "Valor não pode ser zero."


def test_withdraw_deducts_amount_from_balance():
    account = BankAccount("12345678901", 1000.0)

    account.withdraw(500.0)

    assert account.balance == 500.0


def test_withdraw_more_than_balance():
    account = BankAccount("12345678900", 100.0)

    with pytest.raises(BankException) as e:
        account.withdraw(200.0)

    assert str(e.value) == "Saldo insuficiente. Operação não realizada."


def test_withdraw_should_add_withdrawal_transaction_to_statement():
    account = BankAccount("12345678901", 100.0)

    value = 50.0

    account.withdraw(value)

    last_transaction = account.statement[-1]

    assert last_transaction.transaction_type == TransactionType.WITHDRAW
    assert last_transaction.value == value
    assert last_transaction.description == f"Saque de R${value:.2f} da conta."
    assert last_transaction.date is not None


def test_withdraw_with_insufficient_balance_does_not_add_transaction_to_statement():
    account = BankAccount("12345678901", 100.0)

    withdrawal_value = 200.0

    initial_statement_length = len(account.statement)

    with pytest.raises(BankException):
        account.withdraw(withdrawal_value)

    assert len(account.statement) == initial_statement_length


def test_withdraw_with_floating_point_balance():
    account = BankAccount("12345678901", 100.50)

    withdrawal_value = 50.25

    account.withdraw(withdrawal_value)

    assert account.balance == 50.25
    assert len(account.statement) == 1
    assert account.statement[0].value == withdrawal_value
    assert account.statement[0].transaction_type == TransactionType.WITHDRAW
    assert account.statement[0].description == f"Saque de R${withdrawal_value:.2f} da conta."


def test_withdraw_with_floating_point_amount():
    account = BankAccount("12345678901")

    account.deposit(1000.00)
    account.withdraw(500.50)

    assert account.balance == 499.50
    assert len(account.statement) == 2
    assert account.statement[-1].transaction_type == TransactionType.WITHDRAW
    assert account.statement[-1].value == 500.50
    assert account.statement[-1].description == "Saque de R$500.50 da conta."


def test_withdraw_large_amount():
    account = BankAccount("12345678901", 1000000.0)

    initial_balance = account.balance

    large_withdrawal_amount = 999999.99

    account.withdraw(large_withdrawal_amount)

    expected_balance = initial_balance - large_withdrawal_amount

    assert account.balance == expected_balance


def test_withdraw_maximum_allowed_amount():
    account = BankAccount("12345678901")

    initial_balance = 1000.00
    withdrawal_amount = 1000.00

    account.deposit(initial_balance)
    account.withdraw(withdrawal_amount)

    assert account.balance == initial_balance - withdrawal_amount
    assert len(account.statement) == 2
    assert account.statement[-1].transaction_type == TransactionType.WITHDRAW
    assert account.statement[-1].value == withdrawal_amount
    assert account.statement[-1].description == f"Saque de R${withdrawal_amount:.2f} da conta."
