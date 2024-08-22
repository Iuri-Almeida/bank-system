import pytest

from bank.bank import Bank
from bank.bank_exception import BankException


def test_create_account_with_empty_cpf_or_cnpj():
    bank = Bank()

    with pytest.raises(BankException) as e:
        bank.create_account("")

    assert str(e.value) == "CPF/CNPJ não pode estar vazio."


def test_create_account_with_non_string_cpf():
    bank = Bank()

    with pytest.raises(TypeError) as e:
        bank.create_account(12345678901)

    assert str(e.value) == "CPF/CNPJ deve ser uma string."


def test_create_account_with_non_string_cnpj():
    bank = Bank()

    with pytest.raises(TypeError) as e:
        bank.create_account(12345678901234)

    assert str(e.value) == "CPF/CNPJ deve ser uma string."


def test_create_account_with_non_numeric_cpf():
    bank = Bank()

    non_numeric_cpf = "1234567890a"

    with pytest.raises(ValueError) as e:
        bank.create_account(non_numeric_cpf)

    assert str(e.value) == "CPF/CNPJ deve conter apenas dígitos."


def test_create_account_with_non_numeric_cnpj():
    bank = Bank()

    non_numeric_cnpj = "1234567890abcd"

    with pytest.raises(ValueError) as e:
        bank.create_account(non_numeric_cnpj)

    assert str(e.value) == "CPF/CNPJ deve conter apenas dígitos."


def test_create_account_with_cpf_less_than_11_characters():
    bank = Bank()

    with pytest.raises(ValueError) as e:
        bank.create_account("123456789")

    assert str(e.value) == "CPF/CNPJ inválido para o valor '123456789'. CPF deve ter 11 dígitos e CNPJ deve ter 14 dígitos."


def test_create_account_with_cpf_more_than_11_characters():
    bank = Bank()

    with pytest.raises(ValueError) as e:
        bank.create_account("123456789012")

    assert str(e.value) == "CPF/CNPJ inválido para o valor '123456789012'. CPF deve ter 11 dígitos e CNPJ deve ter 14 dígitos."


def test_create_account_with_cnpj_less_than_14_characters():
    bank = Bank()

    with pytest.raises(ValueError) as e:
        bank.create_account("1234567890123")

    assert str(e.value) == "CPF/CNPJ inválido para o valor '1234567890123'. CPF deve ter 11 dígitos e CNPJ deve ter 14 dígitos."


def test_create_account_with_cnpj_more_than_14_characters():
    bank = Bank()

    with pytest.raises(ValueError) as e:
        bank.create_account("123456789012345")

    assert str(e.value) == "CPF/CNPJ inválido para o valor '123456789012345'. CPF deve ter 11 dígitos e CNPJ deve ter 14 dígitos."


def test_create_account_with_existing_cpf():
    bank = Bank()

    cpf = "12345678901"

    existing_account = bank.create_account(cpf)

    with pytest.raises(BankException) as e:
        bank.create_account(cpf)

    assert str(e.value) == f"Conta já cadastrada para o CPF/CNPJ {cpf}."


def test_create_account_with_existing_cnpj():
    bank = Bank()

    cnpj = "12345678901234"

    existing_account = bank.create_account(cnpj)

    with pytest.raises(BankException) as e:
        bank.create_account(cnpj)

    assert str(e.value) == f"Conta já cadastrada para o CPF/CNPJ {cnpj}."


def test_create_account_with_unique_cpf():
    bank = Bank()
    new_account = bank.create_account("98765432109")

    assert new_account.id == "98765432109"
    assert new_account.balance == 0
    assert new_account in bank.accounts.values()


def test_create_account_with_unique_cnpj():
    bank = Bank()
    new_account = bank.create_account("98765432109876")

    assert new_account.id == "98765432109876"
    assert new_account.balance == 0
    assert new_account in bank.accounts.values()
