import pytest

from bank.bank_exception import BankException
from bank.transaction_type import TransactionType
from bank.accounts.personal_account import PersonalAccount
from bank.accounts.legal_entity_account import LegalEntityAccount


def test_transfer_personal_account_none_value_should_raise_exception():
    sender_account = PersonalAccount("12345678901")
    receiver_account = PersonalAccount("09876543210")

    with pytest.raises(BankException) as e:
        sender_account.transfer(receiver_account, None)

    assert str(e.value) == "Valor não pode ser vazio."


def test_transfer_legal_entity_account_none_value_should_raise_exception():
    sender_account = LegalEntityAccount("12345678901234")
    receiver_account = LegalEntityAccount("09876543210987")

    with pytest.raises(BankException) as e:
        sender_account.transfer(receiver_account, None)

    assert str(e.value) == "Valor não pode ser vazio."


def test_transfer_personal_account_zero_value_should_raise_exception():
    sender_account = PersonalAccount("12345678901")
    receiver_account = PersonalAccount("09876543210")

    with pytest.raises(ValueError) as e:
        sender_account.transfer(receiver_account, 0)

    assert str(e.value) == "Valor não pode ser zero."


def test_transfer_legal_entity_account_zero_value_should_raise_exception():
    sender_account = LegalEntityAccount("12345678901234")
    receiver_account = LegalEntityAccount("09876543210987")

    with pytest.raises(ValueError) as e:
        sender_account.transfer(receiver_account, 0)

    assert str(e.value) == "Valor não pode ser zero."


def test_transfer_personal_account_with_negative_value_should_raise_exception():
    account1 = PersonalAccount("12345678901")
    account2 = PersonalAccount("98765432109")

    account1.deposit(100.0)

    with pytest.raises(ValueError) as e:
        account1.transfer(account2, -50.0)

    assert str(e.value) == "Valor não pode ser negativo."


def test_transfer_legal_entity_account_with_negative_value_should_raise_exception():
    account1 = LegalEntityAccount("12345678901234")
    account2 = LegalEntityAccount("09876543210987")

    account1.deposit(100.0)

    with pytest.raises(ValueError) as e:
        account1.transfer(account2, -50.0)

    assert str(e.value) == "Valor não pode ser negativo."


def test_transfer_personal_account_with_value_exceeding_balance_raises_exception():
    account1 = PersonalAccount("12345678901")
    account2 = PersonalAccount("09876543210")

    account1.deposit(1000)

    with pytest.raises(BankException) as e:
        account1.transfer(account2, 1500)

    assert str(e.value) == "Saldo insuficiente. Operação não realizada."


def test_transfer_legal_entity_account_with_value_exceeding_balance_raises_exception():
    account1 = LegalEntityAccount("12345678901234")
    account2 = LegalEntityAccount("09876543210987")

    account1.deposit(1000)

    with pytest.raises(BankException) as e:
        account1.transfer(account2, 1500)

    assert str(e.value) == "Saldo insuficiente. Operação não realizada."


def test_transfer_personal_account_to_same_account_does_not_change_balance():
    account = PersonalAccount("12345678901")

    initial_balance = 100.0
    account.deposit(initial_balance)

    with pytest.raises(BankException) as e:
        account.transfer(account, 50.0)

    assert str(e.value) == "Não é possível transferir para a mesma conta."


def test_transfer_legal_entity_account_to_same_account_does_not_change_balance():
    account = LegalEntityAccount("12345678901234")

    initial_balance = 100.0
    account.deposit(initial_balance)

    with pytest.raises(BankException) as e:
        account.transfer(account, 50.0)

    assert str(e.value) == "Não é possível transferir para a mesma conta."


def test_transfer_personal_account_with_valid_value_updates_balance_of_both_accounts():
    sender_account = PersonalAccount("12345678901")
    receiver_account = PersonalAccount("09876543210")

    initial_sender_balance = 100.0
    initial_receiver_balance = 50.0

    sender_account.deposit(initial_sender_balance)
    receiver_account.deposit(initial_receiver_balance)

    transfer_value = 25.0

    sender_account.transfer(receiver_account, transfer_value)

    taxed_value = transfer_value * (1 - sender_account.tax)

    assert sender_account.balance == initial_sender_balance - transfer_value
    assert receiver_account.balance == initial_receiver_balance + taxed_value


def test_transfer_legal_entity_account_with_valid_value_updates_balance_of_both_accounts():
    sender_account = LegalEntityAccount("12345678901234")
    receiver_account = LegalEntityAccount("09876543210987")

    initial_sender_balance = 100.0
    initial_receiver_balance = 50.0

    sender_account.deposit(initial_sender_balance)
    receiver_account.deposit(initial_receiver_balance)

    transfer_value = 25.0

    sender_account.transfer(receiver_account, transfer_value)

    taxed_value = transfer_value * (1 - sender_account.tax)

    assert sender_account.balance == initial_sender_balance - transfer_value
    assert receiver_account.balance == initial_receiver_balance + taxed_value


def test_transfer_legal_entity_to_personal_account_with_valid_value_updates_balance_of_both_accounts():
    sender_account = LegalEntityAccount("12345678901234")
    receiver_account = PersonalAccount("09876543210")

    initial_sender_balance = 100.0
    initial_receiver_balance = 50.0

    sender_account.deposit(initial_sender_balance)
    receiver_account.deposit(initial_receiver_balance)

    transfer_value = 25.0

    sender_account.transfer(receiver_account, transfer_value)

    taxed_value = transfer_value * (1 - sender_account.tax)

    assert sender_account.balance == initial_sender_balance - transfer_value
    assert receiver_account.balance == initial_receiver_balance + taxed_value


def test_transfer_personal_account_with_valid_value_should_add_entry_in_statement_of_both_accounts():
    sender_account = PersonalAccount("12345678901")
    receiver_account = PersonalAccount("09876543210")

    initial_sender_balance = 100.0
    initial_receiver_balance = 50.0

    value_to_transfer = 30.0

    sender_account.deposit(initial_sender_balance)
    receiver_account.deposit(initial_receiver_balance)

    sender_account.transfer(receiver_account, value_to_transfer)

    sender_transaction = sender_account.statement[-1]
    receiver_transaction = receiver_account.statement[-1]

    taxed_value = value_to_transfer * (1 - sender_account.tax)

    assert sender_transaction.transaction_type == TransactionType.TRANSFER
    assert sender_transaction.value == taxed_value
    assert sender_transaction.description == f"Transferência de R${taxed_value:.2f} para a conta {receiver_account.account_number}"

    assert receiver_transaction.transaction_type == TransactionType.TRANSFER
    assert receiver_transaction.value == taxed_value
    assert receiver_transaction.description == f"Transferência de R${taxed_value:.2f} da conta {sender_account.account_number}"

    assert sender_account.balance == initial_sender_balance - value_to_transfer
    assert receiver_account.balance == initial_receiver_balance + taxed_value


def test_transfer_legal_entity_account_with_valid_value_should_add_entry_in_statement_of_both_accounts():
    sender_account = LegalEntityAccount("12345678901234")
    receiver_account = LegalEntityAccount("09876543210987")

    initial_sender_balance = 100.0
    initial_receiver_balance = 50.0

    value_to_transfer = 30.0

    sender_account.deposit(initial_sender_balance)
    receiver_account.deposit(initial_receiver_balance)

    sender_account.transfer(receiver_account, value_to_transfer)

    sender_transaction = sender_account.statement[-1]
    receiver_transaction = receiver_account.statement[-1]

    taxed_value = value_to_transfer * (1 - sender_account.tax)

    assert sender_transaction.transaction_type == TransactionType.TRANSFER
    assert sender_transaction.value == taxed_value
    assert sender_transaction.description == f"Transferência de R${taxed_value:.2f} para a conta {receiver_account.account_number}"

    assert receiver_transaction.transaction_type == TransactionType.TRANSFER
    assert receiver_transaction.value == taxed_value
    assert receiver_transaction.description == f"Transferência de R${taxed_value:.2f} da conta {sender_account.account_number}"

    assert sender_account.balance == initial_sender_balance - value_to_transfer
    assert receiver_account.balance == initial_receiver_balance + taxed_value


def test_transfer_legal_entity_to_personal_account_with_valid_value_should_add_entry_in_statement_of_both_accounts():
    sender_account = LegalEntityAccount("12345678901234")
    receiver_account = PersonalAccount("09876543210")

    initial_sender_balance = 100.0
    initial_receiver_balance = 50.0

    value_to_transfer = 30.0

    sender_account.deposit(initial_sender_balance)
    receiver_account.deposit(initial_receiver_balance)

    sender_account.transfer(receiver_account, value_to_transfer)

    sender_transaction = sender_account.statement[-1]
    receiver_transaction = receiver_account.statement[-1]

    taxed_value = value_to_transfer * (1 - sender_account.tax)

    assert sender_transaction.transaction_type == TransactionType.TRANSFER
    assert sender_transaction.value == taxed_value
    assert sender_transaction.description == f"Transferência de R${taxed_value:.2f} para a conta {receiver_account.account_number}"

    assert receiver_transaction.transaction_type == TransactionType.TRANSFER
    assert receiver_transaction.value == taxed_value
    assert receiver_transaction.description == f"Transferência de R${taxed_value:.2f} da conta {sender_account.account_number}"

    assert sender_account.balance == initial_sender_balance - value_to_transfer
    assert receiver_account.balance == initial_receiver_balance + taxed_value


def test_transfer_personal_account_with_valid_value_updates_total_transactions():
    account1 = PersonalAccount("12345678901", 100.0)
    account2 = PersonalAccount("09876543210", 50.0)

    initial_balance1 = account1.balance
    initial_balance2 = account2.balance

    value_to_transfer = 50.0

    account1.transfer(account2, value_to_transfer)

    taxed_value = value_to_transfer * (1 - account1.tax)

    assert account1.balance == initial_balance1 - value_to_transfer
    assert account2.balance == initial_balance2 + taxed_value

    assert len(account1.statement) == 1
    assert len(account2.statement) == 1

    assert account1.statement[-1].transaction_type == TransactionType.TRANSFER
    assert account2.statement[-1].transaction_type == TransactionType.TRANSFER


def test_transfer_legal_entity_account_with_valid_value_updates_total_transactions():
    account1 = LegalEntityAccount("12345678901234", 100.0)
    account2 = LegalEntityAccount("09876543210987", 50.0)

    initial_balance1 = account1.balance
    initial_balance2 = account2.balance

    value_to_transfer = 50.0

    account1.transfer(account2, value_to_transfer)

    taxed_value = value_to_transfer * (1 - account1.tax)

    assert account1.balance == initial_balance1 - value_to_transfer
    assert account2.balance == initial_balance2 + taxed_value

    assert len(account1.statement) == 1
    assert len(account2.statement) == 1

    assert account1.statement[-1].transaction_type == TransactionType.TRANSFER
    assert account2.statement[-1].transaction_type == TransactionType.TRANSFER


def test_transfer_legal_entity_to_personal_account_with_valid_value_updates_total_transactions():
    account1 = LegalEntityAccount("12345678901234", 100.0)
    account2 = LegalEntityAccount("09876543210", 50.0)

    initial_balance1 = account1.balance
    initial_balance2 = account2.balance

    value_to_transfer = 50.0

    account1.transfer(account2, value_to_transfer)

    taxed_value = value_to_transfer * (1 - account1.tax)

    assert account1.balance == initial_balance1 - value_to_transfer
    assert account2.balance == initial_balance2 + taxed_value

    assert len(account1.statement) == 1
    assert len(account2.statement) == 1

    assert account1.statement[-1].transaction_type == TransactionType.TRANSFER
    assert account2.statement[-1].transaction_type == TransactionType.TRANSFER
