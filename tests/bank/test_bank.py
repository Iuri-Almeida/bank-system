from bank.bank import Bank


def test_bank_str_root_account():
    bank = Bank()

    root_account = bank.get_account("00000000000")

    str_representation = str(bank)

    assert str_representation == "{'" + root_account.id + "': PersonalAccount('" + root_account.id + "', '" + root_account.agency + "', '" + root_account.account_number + "', " + f"{root_account.balance:.2f}" + ")}"


def test_str_representation_with_diferents_accounts():
    bank = Bank()

    root_account = bank.get_account('00000000000')
    account2 = bank.create_account('23456789012345')

    str_representation = str(bank)

    assert str_representation == "{'" + root_account.id + "': PersonalAccount('" + root_account.id + "', '" + root_account.agency + "', '" + root_account.account_number + "', " + f"{root_account.balance:.2f}" + "), '" + account2.id + "': LegalEntityAccount('" + account2.id + "', '" + account2.agency + "', '" + account2.account_number + "', " + f"{account2.balance:.2f}" + ")}"


def test_str_method_large_decimal_places():
    bank = Bank()

    root_account = bank.get_account('00000000000')

    account1 = bank.create_account("12345678901234")
    account1.deposit(10000000000.123456789)

    str_representation = str(bank)

    assert str_representation == "{'" + root_account.id + "': PersonalAccount('" + root_account.id + "', '" + root_account.agency + "', '" + root_account.account_number + "', " + f"{root_account.balance:.2f}" + "), '" + account1.id + "': LegalEntityAccount('" + account1.id + "', '" + account1.agency + "', '" + account1.account_number + "', " + f"{account1.balance:.2f}" + ")}"


def test_bank_repr_root_account():
    bank = Bank()

    root_account = bank.get_account("00000000000")

    repr_representation = repr(bank)

    assert repr_representation == "Bank({'" + root_account.id + "': PersonalAccount('" + root_account.id + "', '" + root_account.agency + "', '" + root_account.account_number + "', " + f"{root_account.balance:.2f}" + ")})"


def test_bank_repr_with_multiple_accounts():
    bank = Bank()

    account1 = bank.create_account('12345678901')
    account2 = bank.create_account('23456789012')

    repr_representation = repr(bank)

    assert repr_representation == f"Bank({str(bank)})"
