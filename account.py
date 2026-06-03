from decimal import Decimal, InvalidOperation


class Account:
    def __init__(self):
        self.balance = Decimal("0.00")

    def deposit(self, amount):
        amount = self._to_decimal(amount)

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount

    def withdraw(self, amount):
        amount = self._to_decimal(amount)

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount

    def get_balance(self):
        return self.balance

    def _to_decimal(self, amount):
        try:
            return Decimal(str(amount))
        except InvalidOperation:
            raise ValueError("Invalid amount")