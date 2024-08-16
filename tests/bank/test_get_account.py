import pytest

from bank.bank import Bank
from bank.bank_account import BankAccount
from bank.bank_exception import BankException


def test_get_account_raises_exception_when_cpf_does_not_exist():
    bank = Bank()
    cpf_not_registered = "12345678901"

    with pytest.raises(BankException) as e:
        bank.get_account(cpf_not_registered)

    assert str(e.value) == f"Conta não encontrada para o CPF {cpf_not_registered}."


def test_get_account_with_existing_cpf():
    bank = Bank()
    cpf = "12345678901"
    bank.create_account(cpf)

    result = bank.get_account(cpf)

    assert isinstance(result, BankAccount)
    assert result.cpf == cpf


def test_get_account_with_empty_cpf():
    bank = Bank()
    bank.create_account("12345678901")

    with pytest.raises(BankException) as e:
        bank.get_account("")

    assert str(e.value) == "CPF não pode estar vazio."


def test_get_account_raises_exception_when_cpf_is_none():
    bank = Bank()
    bank.create_account("12345678901")

    with pytest.raises(BankException) as e:
        bank.get_account(None)

    assert str(e.value) == "CPF não pode estar vazio."


def test_get_account_handles_leading_and_trailing_whitespaces():
    bank = Bank()

    cpf = "12345678901"

    bank.create_account(cpf)

    with pytest.raises(ValueError) as e1:
        bank.get_account("  " + cpf)
    
    assert str(e1.value) == "CPF deve ter 11 dígitos."

    with pytest.raises(ValueError) as e2:
        bank.get_account("  " + cpf + "  ")
    
    assert str(e2.value) == "CPF deve ter 11 dígitos."

    with pytest.raises(ValueError) as e3:
        bank.get_account(cpf + "  ")
    
    assert str(e3.value) == "CPF deve ter 11 dígitos."


def test_get_account_returns_same_object_for_same_cpf():
    bank = Bank()

    cpf = "12345678901"

    account1 = bank.create_account(cpf)
    account2 = bank.get_account(cpf)

    assert account1 is account2


def test_get_account_raises_exception_when_cpf_is_not_valid():
    bank = Bank()

    bank.create_account("12345678901")

    with pytest.raises(ValueError) as e:
        bank.get_account("1234567890a")

    assert str(e.value) == "CPF deve conter apenas dígitos."
