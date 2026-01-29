import pytest
from oop_bank_account.account import BankAccount


def test_initial_balance():
    account = BankAccount("Alice")
    assert account.get_balance() == 0.0


def test_withdraw_insufficient_balance():
    account = BankAccount("Dave", 50)
    with pytest.raises(ValueError):
        account.withdraw(100)


def test_withdraw_negative_balance():
    account = BankAccount("John", 40)
    with pytest.raises(ValueError):
        account.withdraw(-100)


def test_deposit_incorrect_deposit():
    account = BankAccount("Varun", 0)
    with pytest.raises(ValueError):
        account.deposit(-5)
