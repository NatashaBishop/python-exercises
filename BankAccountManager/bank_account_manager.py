# file: bank_account_manager.py

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
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrew: {amount}. New balance: {self.balance}")

    def get_balance(self) -> float:
        return self.balance


def main():
    account = None

    while True:
        print("\nWelcome to the Bank!")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            if account is not None:
                print("Account already exists.")
                continue
            name = input("Enter your name: ").strip()
            try:
                initial = float(input("Enter initial deposit: "))
            except ValueError:
                print("Invalid number.")
                continue
            account = BankAccount(name, initial)
            print(f"Account created for {name} with balance {initial}")

        elif choice == "2":
            if account is None:
                print("Please create an account first.")
                continue
            try:
                amount = float(input("Enter amount to deposit: "))
            except ValueError:
                print("Invalid number.")
                continue
            account.deposit(amount)

        elif choice == "3":
            if account is None:
                print("Please create an account first.")
                continue
            try:
                amount = float(input("Enter amount to withdraw: "))
            except ValueError:
                print("Invalid number.")
                continue
            account.withdraw(amount)

        elif choice == "4":
            if account is None:
                print("Please create an account first.")
                continue
            print(f"Balance: {account.get_balance()}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
