import pytest

from bank.bank_exception import BankException
from bank.transaction_type import TransactionType
from bank.accounts.personal_account import PersonalAccount
from bank.accounts.legal_entity_account import LegalEntityAccount


def test_withdraw_personal_account_negative_value():
    bank_account = PersonalAccount("12345678901")

    bank_account.deposit(100)

    with pytest.raises(ValueError) as e:
        bank_account.withdraw(-10)
    
    assert str(e.value) == "Valor não pode ser negativo."


def test_withdraw_legal_entity_account_negative_value():
    bank_account = LegalEntityAccount("12345678901234")

    bank_account.deposit(100)

    with pytest.raises(ValueError) as e:
        bank_account.withdraw(-10)
    
    assert str(e.value) == "Valor não pode ser negativo."


def test_withdraw_personal_account_none_value():
    account = PersonalAccount("12345678901")
    account.deposit(100.0)

    with pytest.raises(BankException) as e:
        account.withdraw(None)

    assert str(e.value) == "Valor não pode ser vazio."


def test_withdraw_legal_entity_account_none_value():
    account = LegalEntityAccount("12345678901234")
    account.deposit(100.0)

    with pytest.raises(BankException) as e:
        account.withdraw(None)

    assert str(e.value) == "Valor não pode ser vazio."


def test_withdraw_personal_account_zero_value():
    account = PersonalAccount("12345678901")
    account.deposit(100.0)

    with pytest.raises(ValueError) as e:
        account.withdraw(0)

    assert str(e.value) == "Valor não pode ser zero."


def test_withdraw_legal_entity_account_zero_value():
    account = LegalEntityAccount("12345678901234")
    account.deposit(100.0)

    with pytest.raises(ValueError) as e:
        account.withdraw(0)

    assert str(e.value) == "Valor não pode ser zero."


def test_withdraw_personal_account_deducts_amount_from_balance():
    account = PersonalAccount("12345678901", 1000.0)

    account.withdraw(500.0)

    assert account.balance == 500.0


def test_withdraw_legal_entity_account_deducts_amount_from_balance():
    account = LegalEntityAccount("12345678901234", 1000.0)

    account.withdraw(500.0)

    assert account.balance == 500.0


def test_withdraw_personal_account_more_than_balance():
    account = PersonalAccount("12345678900", 100.0)

    with pytest.raises(BankException) as e:
        account.withdraw(200.0)

    assert str(e.value) == "Saldo insuficiente. Operação não realizada."\


def test_withdraw_legal_entity_account_more_than_balance():
    account = LegalEntityAccount("12345678901234", 100.0)

    with pytest.raises(BankException) as e:
        account.withdraw(200.0)

    assert str(e.value) == "Saldo insuficiente. Operação não realizada."


def test_withdraw_personal_account_should_add_withdrawal_transaction_to_statement():
    account = PersonalAccount("12345678901", 100.0)

    withdrawal_value = 50.0

    account.withdraw(withdrawal_value)

    taxed_value = withdrawal_value * (1 - account.tax)

    last_transaction = account.statement[-1]

    assert last_transaction.transaction_type == TransactionType.WITHDRAW
    assert last_transaction.value == taxed_value
    assert last_transaction.description == f"Saque de R${taxed_value:.2f} da conta."
    assert last_transaction.date is not None


def test_withdraw_legal_entity_should_add_withdrawal_transaction_to_statement():
    account = LegalEntityAccount("12345678901234", 100.0)

    withdrawal_value = 50.0

    account.withdraw(withdrawal_value)

    taxed_value = withdrawal_value * (1 - account.tax)

    last_transaction = account.statement[-1]

    assert last_transaction.transaction_type == TransactionType.WITHDRAW
    assert last_transaction.value == taxed_value
    assert last_transaction.description == f"Saque de R${taxed_value:.2f} da conta."
    assert last_transaction.date is not None


def test_withdraw_personal_account_with_insufficient_balance_does_not_add_transaction_to_statement():
    account = PersonalAccount("12345678901", 100.0)

    withdrawal_value = 200.0

    initial_statement_length = len(account.statement)

    with pytest.raises(BankException):
        account.withdraw(withdrawal_value)

    assert len(account.statement) == initial_statement_length


def test_withdraw_legal_entity_account_with_insufficient_balance_does_not_add_transaction_to_statement():
    account = LegalEntityAccount("12345678901234", 100.0)

    withdrawal_value = 200.0

    initial_statement_length = len(account.statement)

    with pytest.raises(BankException):
        account.withdraw(withdrawal_value)

    assert len(account.statement) == initial_statement_length


def test_withdraw_personal_account_with_floating_point_balance():
    account = PersonalAccount("12345678901", 100.50)

    withdrawal_value = 50.25

    account.withdraw(withdrawal_value)

    taxed_value = withdrawal_value * (1 - account.tax)

    assert account.balance == 50.25
    assert len(account.statement) == 1
    assert account.statement[0].value == taxed_value
    assert account.statement[0].transaction_type == TransactionType.WITHDRAW
    assert account.statement[0].description == f"Saque de R${taxed_value:.2f} da conta."


def test_withdraw_legal_entity_account_with_floating_point_balance():
    account = LegalEntityAccount("12345678901234", 100.50)

    withdrawal_value = 50.25

    account.withdraw(withdrawal_value)

    taxed_value = withdrawal_value * (1 - account.tax)

    assert account.balance == 50.25
    assert len(account.statement) == 1
    assert account.statement[0].value == taxed_value
    assert account.statement[0].transaction_type == TransactionType.WITHDRAW
    assert account.statement[0].description == f"Saque de R${taxed_value:.2f} da conta."


def test_withdraw_personal_account_with_floating_point_amount():
    account = PersonalAccount("12345678901")

    withdrawal_value = 500.50

    account.deposit(1000.00)
    account.withdraw(withdrawal_value)

    taxed_value = withdrawal_value * (1 - account.tax)

    assert account.balance == 499.50
    assert len(account.statement) == 2
    assert account.statement[-1].transaction_type == TransactionType.WITHDRAW
    assert account.statement[-1].value == taxed_value
    assert account.statement[-1].description == f"Saque de R${taxed_value:.2f} da conta."


def test_withdraw_legal_entity_account_with_floating_point_amount():
    account = LegalEntityAccount("12345678901234")

    withdrawal_value = 500.50

    account.deposit(1000.00)
    account.withdraw(withdrawal_value)

    taxed_value = withdrawal_value * (1 - account.tax)

    assert account.balance == 499.50
    assert len(account.statement) == 2
    assert account.statement[-1].transaction_type == TransactionType.WITHDRAW
    assert account.statement[-1].value == taxed_value
    assert account.statement[-1].description == f"Saque de R${taxed_value:.2f} da conta."


def test_withdraw_personal_account_large_amount():
    account = PersonalAccount("12345678901", 1000000.0)

    initial_balance = account.balance

    large_withdrawal_amount = 999999.99

    account.withdraw(large_withdrawal_amount)

    expected_balance = initial_balance - large_withdrawal_amount

    assert account.balance == expected_balance


def test_withdraw_legal_entity_account_large_amount():
    account = LegalEntityAccount("12345678901234", 1000000.0)

    initial_balance = account.balance

    large_withdrawal_amount = 999999.99

    account.withdraw(large_withdrawal_amount)

    expected_balance = initial_balance - large_withdrawal_amount

    assert account.balance == expected_balance


def test_withdraw_personal_account_maximum_allowed_amount():
    account = PersonalAccount("12345678901")

    initial_balance = 1000.00
    withdrawal_amount = 1000.00

    account.deposit(initial_balance)
    account.withdraw(withdrawal_amount)

    taxed_value = withdrawal_amount * (1 - account.tax)

    assert account.balance == initial_balance - withdrawal_amount
    assert len(account.statement) == 2
    assert account.statement[-1].transaction_type == TransactionType.WITHDRAW
    assert account.statement[-1].value == taxed_value
    assert account.statement[-1].description == f"Saque de R${taxed_value:.2f} da conta."


def test_withdraw_legal_entity_account_maximum_allowed_amount():
    account = LegalEntityAccount("12345678901234")

    initial_balance = 1000.00
    withdrawal_amount = 1000.00

    account.deposit(initial_balance)
    account.withdraw(withdrawal_amount)

    taxed_value = withdrawal_amount * (1 - account.tax)

    assert account.balance == initial_balance - withdrawal_amount
    assert len(account.statement) == 2
    assert account.statement[-1].transaction_type == TransactionType.WITHDRAW
    assert account.statement[-1].value == taxed_value
    assert account.statement[-1].description == f"Saque de R${taxed_value:.2f} da conta."
