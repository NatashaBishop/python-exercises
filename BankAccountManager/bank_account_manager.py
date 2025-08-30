# file: bank_account_manager.py

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        # Keep track of the account owner and starting balance
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        # stop invalid deposits (zero or negative) to ensure balance is positive
        if amount <= 0:
            print("Deposit must be greater than zero.")
            return

        # validate and increase balance    
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
    print("=== Starting Bank Account Manager App=== \n Please input your request: ")
    print("1) List accounts")
    print("2) Create account")
    print("3) Select account")
    print("4) Deposit (selected)")
    print("5) Withdraw (selected)")
    print("6) Check balance (selected)")
    print("7) Show history (selected)")
    print("8) Save")
    print("9) Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            names = bank.list_accounts()
            if not names:
                print("No accounts yet.")
            else:
                for i, name in enumerate(sorted(names), 1):
                    marker = " *" if selected and selected.owner == name else ""
                    print(f"{i}. {name}{marker}")

        elif choice == "2":
            owner = read_nonempty("Owner name: ")
            initial = 0.0
            raw = input("Initial deposit (press Enter for 0): ").strip()
            if raw:
                try:
                    initial = float(raw)
                    if initial < 0:
                        print("Initial deposit cannot be negative.")
                        continue
                except ValueError:
                    print("Invalid number.")
                    continue
            try:
                acct = bank.create_account(owner, initial)
                selected = acct
                bank.save(DATA_FILE)  # autosave
                print(f"Created account for '{acct.owner}' with balance {acct.balance:.2f}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            owner = read_nonempty("Select by owner name: ")
            acct = bank.get_account(owner)
            if not acct:
                print("Account not found.")
            else:
                selected = acct
                print(f"Selected: {selected.owner}")

        elif choice == "4":
            if not selected:
                print("Select an account first.")
                continue
            amount = read_positive_float("Amount to deposit: ")
            try:
                new_bal = selected.deposit(amount)
                bank.save(DATA_FILE)
                print(f"Deposited {amount:.2f}. New balance: {new_bal:.2f}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "5":
            if not selected:
                print("Select an account first.")
                continue
            amount = read_positive_float("Amount to withdraw: ")
            try:
                new_bal = selected.withdraw(amount)
                bank.save(DATA_FILE)
                print(f"Withdrew {amount:.2f}. New balance: {new_bal:.2f}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "6":
            if not selected:
                print("Select an account first.")
                continue
            print(f"Balance for {selected.owner}: {selected.balance:.2f}")

        elif choice == "7":
            if not selected:
                print("Select an account first.")
                continue
            print(f"
History for {selected.owner}:")
            if not selected.transactions:
                print("(no transactions)")
            else:
                for i, t in enumerate(selected.transactions, 1):
                    print(
                        f"{i:02d}. {t.timestamp} | {t.kind:<8} | amt={t.amount:.2f} | bal={t.balance_after:.2f}"
                        + (f" | {t.note}" if t.note else "")
                    )

        elif choice == "8":
            bank.save(DATA_FILE)
            print("Saved.")

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
