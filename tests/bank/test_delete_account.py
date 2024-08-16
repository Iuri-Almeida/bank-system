import pytest

from bank.bank import Bank
from bank.bank_exception import BankException


def test_delete_account_non_existent_cpf():
    bank = Bank()

    with pytest.raises(BankException) as context:
        bank.delete_account("12345678901")

    assert str(context.value) == "Conta não encontrada para o CPF/CNPJ 12345678901."


def test_delete_account_with_nonzero_balance():
    bank = Bank()

    account = bank.create_account("12345678900")

    bank.deposit(account.id, 100)

    with pytest.raises(BankException) as e:
        bank.delete_account(account.id)

    assert str(e.value) == f"Não é possível excluir a conta {account.id} com saldo não zero."
    assert account.id in bank.accounts


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

    bank.deposit(account.id, 100)
    bank.withdraw(account.id, 100)

    deleted_account = bank.delete_account(account.id)

    assert deleted_account == account
    assert account.id not in bank.accounts


def test_delete_account_after_multiple_transactions():
    bank = Bank()

    account1 = bank.create_account("12345678901")
    account2 = bank.create_account("98765432109")

    bank.deposit(account1.id, 1000)
    bank.withdraw(account1.id, 500)
    bank.transfer(account1.id, account2.id, 200)

    assert bank.get_account(account1.id).balance == 300
    assert bank.get_account(account2.id).balance == 200

    bank.withdraw(account1.id, 300)

    deleted_account = bank.delete_account(account1.id)

    assert deleted_account.id == account1.id
    assert deleted_account.balance == 0
    assert account1.id not in bank.accounts



