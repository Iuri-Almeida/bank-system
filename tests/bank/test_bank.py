from bank.bank import Bank


def test_bank_str_no_accounts():
    bank = Bank()

    str_representation = str(bank)

    assert str_representation == "{}"


def test_str_representation_with_accounts():
    bank = Bank()

    account1 = bank.create_account('12345678901')
    account2 = bank.create_account('23456789012')

    str_representation = str(bank)

    assert str_representation == "{'" + account1.id + "': BankAccount('" + account1.id + "', '" + account1.agency + "', '" + account1.account_number + "', " + f"{account1.balance:.2f}" + "), '" + account2.id + "': BankAccount('" + account2.id + "', '" + account2.agency + "', '" + account2.account_number + "', " + f"{account2.balance:.2f}" + ")}"


def test_str_method_large_decimal_places():
    bank = Bank()

    account1 = bank.create_account("12345678901")
    account1.deposit(10000000000.123456789)

    str_representation = str(bank)

    assert str_representation == "{'" + account1.id + "': BankAccount('" + account1.id + "', '" + account1.agency + "', '" + account1.account_number + "', " + f"{account1.balance:.2f}" + ")}"


def test_bank_repr_no_accounts():
    bank = Bank()

    repr_representation = repr(bank)

    assert repr_representation == "Bank({})"


def test_bank_repr_with_multiple_accounts():
    bank = Bank()

    account1 = bank.create_account('12345678901')
    account2 = bank.create_account('23456789012')

    repr_representation = repr(bank)

    assert repr_representation == f"Bank({str(bank)})"
