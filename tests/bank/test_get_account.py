import pytest

from bank.bank import Bank
from bank.bank_account import BankAccount


def test_get_account_raises_exception_when_cpf_does_not_exist():
    bank = Bank()
    cpf_not_registered = "12345678901"

    with pytest.raises(ValueError) as e:
        bank.get_account(cpf_not_registered)

    assert str(e.value) == f"Conta não encontrada para o CPF/CNPJ {cpf_not_registered}."


def test_get_account_raises_exception_when_cnpj_does_not_exist():
    bank = Bank()
    cnpj_not_registered = "12345678901234"

    with pytest.raises(ValueError) as e:
        bank.get_account(cnpj_not_registered)

    assert str(e.value) == f"Conta não encontrada para o CPF/CNPJ {cnpj_not_registered}."


def test_get_account_with_existing_cpf():
    bank = Bank()
    cpf = "12345678901"
    bank.create_account(cpf)

    result = bank.get_account(cpf)

    assert isinstance(result, BankAccount)
    assert result.id == cpf


def test_get_account_with_existing_cnpj():
    bank = Bank()
    cnpj = "12345678901234"
    bank.create_account(cnpj)

    result = bank.get_account(cnpj)

    assert isinstance(result, BankAccount)
    assert result.id == cnpj


def test_get_account_with_empty_cpf():
    bank = Bank()
    bank.create_account("12345678901")

    with pytest.raises(ValueError) as e:
        bank.get_account("")

    assert str(e.value) == f"Conta não encontrada para o CPF/CNPJ ."


def test_get_account_with_empty_cnpj():
    bank = Bank()
    bank.create_account("12345678901234")

    with pytest.raises(ValueError) as e:
        bank.get_account("")

    assert str(e.value) == f"Conta não encontrada para o CPF/CNPJ ."


def test_get_account_raises_exception_when_cpf_is_none():
    bank = Bank()
    bank.create_account("12345678901")

    with pytest.raises(ValueError) as e:
        bank.get_account(None)

    assert str(e.value) == "Conta não encontrada para o CPF/CNPJ None."


def test_get_account_raises_exception_when_cnpj_is_none():
    bank = Bank()
    bank.create_account("12345678901234")

    with pytest.raises(ValueError) as e:
        bank.get_account(None)

    assert str(e.value) == "Conta não encontrada para o CPF/CNPJ None."


def test_get_account_handles_leading_and_trailing_whitespaces():
    bank = Bank()

    cpf = "12345678901"

    bank.create_account(cpf)

    l_whitespaces = "  " + cpf
    with pytest.raises(ValueError) as e1:
        bank.get_account(l_whitespaces)

    assert str(e1.value) == f"Conta não encontrada para o CPF/CNPJ {l_whitespaces}."

    l_r_whitespaces = "  " + cpf + "  "
    with pytest.raises(ValueError) as e2:
        bank.get_account(l_r_whitespaces)

    assert str(e2.value) == f"Conta não encontrada para o CPF/CNPJ {l_r_whitespaces}."

    r_whitespaces = cpf + "  "
    with pytest.raises(ValueError) as e3:
        bank.get_account(r_whitespaces)

    assert str(e3.value) == f"Conta não encontrada para o CPF/CNPJ {r_whitespaces}."


def test_get_account_returns_same_object_for_same_cpf():
    bank = Bank()

    cpf = "12345678901"

    account1 = bank.create_account(cpf)
    account2 = bank.get_account(cpf)

    assert account1 is account2


def test_get_account_returns_same_object_for_same_cnpj():
    bank = Bank()

    cnpj = "12345678901234"

    account1 = bank.create_account(cnpj)
    account2 = bank.get_account(cnpj)

    assert account1 is account2


def test_get_account_raises_exception_when_cpf_is_not_valid():
    bank = Bank()

    bank.create_account("12345678901")

    with pytest.raises(ValueError) as e:
        bank.get_account("1234567890a")

    assert str(e.value) == "Conta não encontrada para o CPF/CNPJ 1234567890a."


def test_get_account_raises_exception_when_cnpj_is_not_valid():
    bank = Bank()

    bank.create_account("12345678901234")

    with pytest.raises(ValueError) as e:
        bank.get_account("1234567890abcd")

    assert str(e.value) == "Conta não encontrada para o CPF/CNPJ 1234567890abcd."
