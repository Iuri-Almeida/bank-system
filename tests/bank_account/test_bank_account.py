import pytest

from bank.accounts.personal_account import PersonalAccount
from bank.accounts.legal_entity_account import LegalEntityAccount


def test_should_raise_exception_when_creating_personal_account_with_negative_balance():
    balance = -100.0

    with pytest.raises(ValueError) as e:
        PersonalAccount("12345678901", balance)

    assert str(e.value) == "O saldo não pode ser negativo."


def test_should_raise_exception_when_creating_legal_entity_account_with_negative_balance():
    balance = -100.0

    with pytest.raises(ValueError) as e:
        LegalEntityAccount("12345678901234", balance)

    assert str(e.value) == "O saldo não pode ser negativo."


def test_str_personal_account_representation():
    account = PersonalAccount("12345678901", 1000.0)

    assert str(account) == f"CPF: {account.id}\nAgência: {account.agency}\nConta: {account.account_number}\nSaldo: R${account.balance:.2f}"


def test_str_legal_entity_account_representation():
    account = LegalEntityAccount("12345678901234", 1000.0)

    assert str(account) == f"CNPJ: {account.id}\nAgência: {account.agency}\nConta: {account.account_number}\nSaldo: R${account.balance:.2f}"


def test_str_personal_account_method_large_decimal_places():
    account = PersonalAccount("12345678901", 10000000000.123456789)

    str_representation = str(account)

    assert str_representation == f"CPF: {account.id}\nAgência: {account.agency}\nConta: {account.account_number}\nSaldo: R${account.balance:.2f}"


def test_str_legal_entity_account_method_large_decimal_places():
    account = LegalEntityAccount("12345678901234", 10000000000.123456789)

    str_representation = str(account)

    assert str_representation == f"CNPJ: {account.id}\nAgência: {account.agency}\nConta: {account.account_number}\nSaldo: R${account.balance:.2f}"


def test_repr_personal_account_method():
    account = PersonalAccount("12345678901", 1000.0)

    repr_representation = repr(account)

    assert repr_representation == f"PersonalAccount('{account.id}', '{account.agency}', '{account.account_number}', {account.balance:.2f})"


def test_repr_legal_entity_account_method():
    account = LegalEntityAccount("12345678901", 1000.0)

    repr_representation = repr(account)

    assert repr_representation == f"LegalEntityAccount('{account.id}', '{account.agency}', '{account.account_number}', {account.balance:.2f})"
