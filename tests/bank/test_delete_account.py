import pytest

from bank.bank import Bank
from bank.bank_exception import BankException


def test_delete_account_non_existent_cpf():
    bank = Bank()

    with pytest.raises(BankException) as context:
        bank.delete_account("12345678901")

    assert str(context.value) == "Conta não encontrada para o CPF 12345678901."


def test_delete_account_with_nonzero_balance():
    bank = Bank()

    account = bank.create_account("12345678900")

    bank.deposit(account.cpf, 100)

    with pytest.raises(BankException) as e:
        bank.delete_account(account.cpf)

    assert str(e.value) == f"Não é possível excluir a conta {account.cpf} com saldo não zero."
    assert account.cpf in bank.accounts


def test_delete_account_with_zero_balance():
    bank = Bank()

    cpf = "12345678901"

    account = bank.create_account(cpf)

    deleted_account = bank.delete_account(cpf)

    assert deleted_account == account
    assert cpf not in bank.accounts
    assert deleted_account.balance == 0


def test_delete_account_after_successful_withdrawal():
    bank = Bank()

    account = bank.create_account("12345678901")

    bank.deposit(account.cpf, 100)
    bank.withdraw(account.cpf, 100)

    deleted_account = bank.delete_account(account.cpf)

    assert deleted_account == account
    assert account.cpf not in bank.accounts


def test_delete_account_after_multiple_transactions():
    bank = Bank()

    account1 = bank.create_account("12345678901")
    account2 = bank.create_account("98765432109")

    bank.deposit(account1.cpf, 1000)
    bank.withdraw(account1.cpf, 500)
    bank.transfer(account1.cpf, account2.cpf, 200)

    assert bank.get_account(account1.cpf).balance == 300
    assert bank.get_account(account2.cpf).balance == 200

    bank.withdraw(account1.cpf, 300)

    deleted_account = bank.delete_account(account1.cpf)

    assert deleted_account.cpf == account1.cpf
    assert deleted_account.balance == 0
    assert account1.cpf not in bank.accounts



