class BankAccount:
    def __init__(self, new_owner, balance=0):
        self._owner = new_owner
        self.__balance = balance

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner_val):
        self._owner = owner_val

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("You cannot input a negative amount")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("You cannot use a negative amount")
        if amount > self.__balance:
            raise ValueError("Not enough founds")
        self.__balance -= amount

    def __str__(self):
        return f"{self._owner} has a balance of ${self.__balance}"

    def __repr__(self):
        return f"BankAccount({self._owner}, {self.__balance})"

if __name__ == "__main__":
    bank_account = BankAccount("John", 500)
    print(bank_account)
    bank_account.deposit(300)
    print(bank_account)
    bank_account.withdraw(400)
    print(bank_account)
    print(bank_account.__repr__())