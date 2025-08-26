class BankAccount:
def __init__(self, owner: str, balance: float = 0.0):
self.owner = owner
self.balance = balance


def deposit(self, amount: float) -> None:
if amount <= 0:
print("Deposit must be greater than zero.")
return
self.balance += amount
print(f"Deposited: {amount}. New balance: {self.balance}")


def withdraw(self, amount: float) -> None:
if amount <= 0:
print("Withdrawal must be greater than zero.")
return
self.balance -= amount
print(f"Withdrew: {amount}. New balance: {self.balance}")
