import pytest
from decimal import Decimal
from account import Account


def test_initial_balance_is_zero():
    account = Account()

    assert account.get_balance() == Decimal("0.00")


def test_deposit_increases_balance():
    account = Account()

    account.deposit("10.50")

    assert account.get_balance() == Decimal("10.50")


def test_multiple_deposits_update_balance():
    account = Account()

    account.deposit("3.10")
    account.deposit("3.20")

    assert account.get_balance() == Decimal("6.30")


def test_withdraw_decreases_balance():
    account = Account()

    account.deposit("20.00")
    account.withdraw("5.25")

    assert account.get_balance() == Decimal("14.75")


def test_cannot_withdraw_more_than_balance():
    account = Account()

    account.deposit("10.00")

    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw("15.00")


def test_cannot_deposit_zero_or_negative_amount():
    account = Account()

    with pytest.raises(ValueError):
        account.deposit("0")

    with pytest.raises(ValueError):
        account.deposit("-5.00")


def test_cannot_withdraw_zero_or_negative_amount():
    account = Account()

    with pytest.raises(ValueError):
        account.withdraw("0")

    with pytest.raises(ValueError):
        account.withdraw("-5.00")


def test_invalid_amount_raises_error():
    account = Account()

    with pytest.raises(ValueError):
        account.deposit("abc")