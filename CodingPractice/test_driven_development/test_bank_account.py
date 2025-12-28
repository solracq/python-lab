"""
Test Scenarios:
Account starts with 0 balance.
deposit(100) updates balance to 100.
withdraw(50) reduces balance (balance 50).
Negative deposits/withdrawals throw.
Add transaction record for each deposit/withdrawal (date, amount, balance).
printStatement() returns formatted lines (most recent first).
Add transfer(Account target, amount) that withdraws and deposits atomically.
Add daily interest calculation method (optional).
"""
import pytest
from bank_account import Account
from bank_account import FixedClock

@pytest.fixture
def acct():
    return Account()

# @pytest.fixture
# def clock():
#     return FixedClock()

def test_new_account_has_zero_balance(acct):
    assert acct.balance == 0

def test_deposit_increases_balance(acct):
    acct.deposit(100)
    assert acct.balance == 100

def test_withdraw_decreases_balance(acct):
    acct.deposit(100)
    acct.withdraw(50)
    assert acct.balance == 50

def test_deposit_negative_raises_error(acct):
    with pytest.raises(ValueError) as execinfo:
        acct.deposit(-10)
    assert "You cannot use a negative amount" in str(execinfo.value)

def test_withdraw_negative_raises_error(acct):
    with pytest.raises(ValueError) as execinfo:
        acct.withdraw(-5)
    assert "You cannot use a negative amount" in str(execinfo.value)

def test_deposit_record_transaction(acct):
    acct.deposit(100)
    assert len(acct.transactions) == 1
    transaction = acct.transactions[0]
    assert transaction.amount == 100
    assert transaction.balance_after == 100
    assert hasattr(transaction, "date")

def test_print_statement_header_transactions(acct):
    acct.deposit(100)
    acct.withdraw(30)
    txt = acct.print_statement()
    assert "Date | Amount | Balance" in txt
    # Assert most recent transactions: withdraw -> deposit
    assert txt.splitlines()[1].endswith("30 | 70")

def test_transactions_have_deterministic_dates_with_fixed_clock():
    clock = FixedClock("2025-01-01T10:00:00")
    acct = Account(clock=clock)
    acct.deposit(50)
    assert acct.transactions[0].date.isoformat() == "2025-01-01T10:00:00"

def test_transfer_moves_money_and_records_transactions():
    a = Account()
    b = Account()
    a.deposit(300)
    a.transfer(b, 120)
    assert a.balance == 180
    assert b.balance == 120
    assert a.transactions[-1].amount == 120
    assert b.transactions[-1].amount == 120