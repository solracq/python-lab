"""
Bank Account with Transactions
Goal: OO design for Account with deposit, withdraw, and transaction history; print statement.

Design & implementation hints
Model "Transaction" as a value object with date, amount, balanceAfter.
"Account" manages balance and appends Transactions.
For printStatement, decouple formatting from account logic (use "StatementPrinter" interface): helps testability (mock printer).
Use dependency injection for clock/time provider to make dates deterministic in tests -> "Clock" abstraction.
"""
from datetime import datetime

class Transactions:
    def __init__(self, date: datetime, amount: int, balance_after: int):
        self.date = date
        self.amount = amount
        self.balance_after = balance_after

class StatementPrinter:
    HEADER = "Date | Amount | Balance"

    def format(self, transactions: list[Transactions]) -> str:
        lines = [self.HEADER]
        for t in reversed(transactions):
            lines.append(f"{t.date.isoformat()} | {t.amount} | {t.balance_after}")
        return "\n".join(lines)

class Clock:
    def now(self) -> datetime:
        from datetime import datetime
        return datetime.now()

class FixedClock(Clock):
    def __init__(self, iso_ts):
        from datetime import datetime
        self._dt = datetime.fromisoformat(iso_ts)

    def now(self):
        return self._dt

class Account:
    def __init__(self, clock: Clock = None):
        self.balance = 0
        self.transactions = []
        self.clock = clock or Clock()

    # Helpers
    def _validate_amount(self, amount: int):
        if amount < 0:
            raise ValueError("You cannot use a negative amount")

    def _now(self):
        # return datetime.now()
        return self.clock.now()

    def _record_transaction(self, date: datetime, amount: int, balance:int):
        transaction = Transactions(date, amount, balance)
        self.transactions.append(transaction)

    # Actions
    def deposit(self, amount: int):
        self._validate_amount(amount)
        self.balance += amount
        self._record_transaction(self._now(), amount, self.balance)

    def withdraw(self, amount: int):
        self._validate_amount(amount)
        self.balance -= amount
        self._record_transaction(self._now(), amount, self.balance)

    def print_statement(self, printer=None):
        if printer is None:
            printer = StatementPrinter()
        return printer.format(self.transactions)

    def transfer(self, target: "Account", amount: int):
        self._validate_amount(amount)
        self.withdraw(amount)
        try:
            target.deposit(amount)
        except Exception:
            self.deposit(amount)
            raise
