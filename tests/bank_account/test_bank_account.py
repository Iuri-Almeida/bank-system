import pytest

from bank.bank_account import BankAccount


def test_should_raise_exception_when_creating_bank_account_with_negative_balance():
    balance = -100.0

    with pytest.raises(ValueError) as e:
        BankAccount("12345678901", balance)

    assert str(e.value) == "O saldo não pode ser negativo."


def test_str_representation():
    account = BankAccount("12345678901", 1000.0)

    assert str(account) == f"CPF/CNPJ: {account.id}\nAgência: {account.agency}\nConta: {account.account_number}\nSaldo: R${account.balance:.2f}"


def test_str_method_large_decimal_places():
    account = BankAccount("12345678901", 10000000000.123456789)

    str_representation = str(account)

    assert str_representation == f"CPF/CNPJ: {account.id}\nAgência: {account.agency}\nConta: {account.account_number}\nSaldo: R${account.balance:.2f}"


def test_repr_method():
    account = BankAccount("12345678901", 1000.0)

    repr_representation = repr(account)

    assert repr_representation == f"BankAccount('{account.id}', '{account.agency}', '{account.account_number}', {account.balance:.2f})"
