# Question: Bank Account Class
# Create a Python class called BankAccount that represents a simple bank account. The class should have the following methods:

# 1.__init__(self, owner, balance): Initializes the account with an owner's name and an initial balance.
# 2.deposit(self, amount): Adds the specified amount to the account balance.
# 3.withdraw(self, amount): Subtracts the specified amount from the account balance. If the balance is insufficient, print a message indicating that the withdrawal cannot be completed.
# 4.get_balance(self): Returns the current balance of the account.
# 5.get_owner(self): Returns the owner's name of the account.


class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance

    def deposite(self, ammount):
        self._balance += ammount

    def withdraw(self, ammount):
        self._balance -= ammount

    def get_balance(self):
        print(f"The Total balance is: {self._balance}")

    def get_owner(self):
        print(f"The Banks Owner Name: {self._owner!r}")


account1 = BankAccount("Naim", 1000)

account1.deposite(500)
account1.withdraw(200)

account1.get_balance()
account1.get_owner()
