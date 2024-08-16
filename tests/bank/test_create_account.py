import pytest

from bank.bank import Bank
from bank.bank_exception import BankException


def test_create_account_with_empty_cpf():
    bank = Bank()

    with pytest.raises(BankException) as e:
        bank.create_account("")

    assert str(e.value) == "CPF não pode estar vazio."


def test_create_account_with_non_string_cpf():
    bank = Bank()

    with pytest.raises(TypeError) as e:
        bank.create_account(12345678901)

    assert str(e.value) == "CPF deve ser uma string."


def test_create_account_with_non_numeric_cpf():
    bank = Bank()

    non_numeric_cpf = "1234567890a"

    with pytest.raises(ValueError) as e:
        bank.create_account(non_numeric_cpf)

    assert str(e.value) == "CPF deve conter apenas dígitos."


def test_create_account_with_cpf_less_than_11_characters():
    bank = Bank()

    with pytest.raises(ValueError) as e:
        bank.create_account("123456789")

    assert str(e.value) == "CPF deve ter 11 dígitos."


def test_create_account_with_cpf_more_than_11_characters():
    bank = Bank()

    with pytest.raises(ValueError) as e:
        bank.create_account("123456789012")

    assert str(e.value) == "CPF deve ter 11 dígitos."


def test_create_account_with_existing_cpf():
    bank = Bank()
    existing_account = bank.create_account("12345678901")

    with pytest.raises(BankException) as e:
        bank.create_account("12345678901")

    assert str(e.value) == "Conta já cadastrada para o CPF 12345678901."


def test_create_account_with_unique_cpf():
    bank = Bank()
    new_account = bank.create_account("98765432109")

    assert new_account.id == "98765432109"
    assert new_account.balance == 0
    assert new_account in bank.accounts.values()
