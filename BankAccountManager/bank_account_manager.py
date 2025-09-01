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
    # Prevent invalid withdrawals (zero or negative values) to maintain data integrity
    if amount <= 0:
        print("Withdrawal must be greater than zero.")
        return

    # Block withdrawal attempts larger than the available balance
    if amount > self.balance:
        print("Insufficient funds.")
        return

    # save withdrawal , print the balance
    self.balance -= amount
    print(f"Withdrew: {amount}. New balance: {self.balance}")

def get_balance(self) -> float:
    return self.balance  # return current balance 

# start running banking application
def main():
    account = None

while True:
    # Main application menu: loop ensures user can perform multiple actions until exit
    print("=== Starting Bank Account Manager App=== \n Please input your request: ")

    # Options are numbered for simple navigation and clarity
    print("1) List accounts")         # Useful for seeing all existing accounts
    print("2) Create account")       # Allows user to open a new account
    print("3) Select account")       # Choose an account to perform operations on
    print("4) Deposit (selected)")   # Add money to the chosen account
    print("5) Withdraw (selected)")  # Remove money, with safeguards
    print("6) Check balance (selected)")  # View current funds
    print("7) Show history (selected)")   # See past transactions
    print("8) Save")                 # Persist accounts to storage
    print("9) Exit")                 # Quit the program safely


 choice = input("Choose an option: ").strip()  # Read user input and remove extra spaces

if choice == "1":
    # Show all accounts; mark currently selected one with "*"
    names = bank.list_accounts()
    if not names:
        print("No accounts yet.")  # Feedback if bank is empty
    else:
        for i, name in enumerate(sorted(names), 1):
            marker = " *" if selected and selected.owner == name else ""
            print(f"{i}. {name}{marker}")

elif choice == "2":
    # Create a new account with optional initial deposit
    owner = read_nonempty("Owner name: ")
    initial = 0.0
    raw = input("Initial deposit (press Enter for 0): ").strip()
    if raw:
        try:
            initial = float(raw)
            if initial < 0:
                print("Initial deposit cannot be negative.")  # Guard against invalid input
                continue
        except ValueError:
            print("Invalid number.")  # Handle non-numeric input
            continue
    try:
        acct = bank.create_account(owner, initial)
        selected = acct  # Auto-select new account
        bank.save(DATA_FILE)  # Autosave ensures persistence
        print(f"Created account for '{acct.owner}' with balance {acct.balance:.2f}")
    except ValueError as e:
        print(f"Error: {e}")  # Handle duplicate account creation

elif choice == "3":
    # Switch to an existing account
    owner = read_nonempty("Select by owner name: ")
    acct = bank.get_account(owner)
    if not acct:
        print("Account not found.")  # User tried to select non-existing account
    else:
        selected = acct
        print(f"Selected: {selected.owner}")

elif choice == "4":
    # Deposit money into selected account
    if not selected:
        print("Select an account first.")  # Prevent deposit with no target
        continue
    amount = read_positive_float("Amount to deposit: ")
    try:
        new_bal = selected.deposit(amount)
        bank.save(DATA_FILE)  # Autosave after balance change
        print(f"Deposited {amount:.2f}. New balance: {new_bal:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

elif choice == "5":
    # Withdraw money from selected account
    if not selected:
        print("Select an account first.")  # Prevent withdrawal with no target
        continue
    amount = read_positive_float("Amount to withdraw: ")
    try:
        new_bal = selected.withdraw(amount)
        bank.save(DATA_FILE)  # Autosave after balance change
        print(f"Withdrew {amount:.2f}. New balance: {new_bal:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

elif choice == "6":
    # Check balance of selected account
    if not selected:
        print("Select an account first.")
        continue
    print(f"Balance for {selected.owner}: {selected.balance:.2f}")

elif choice == "7":
    # Display transaction history for selected account
    if not selected:
        print("Select an account first.")
        continueprint(f"\nHistory for {selected.owner}:")
# Show transaction history for the selected account
if not selected.transactions:
    print("(no transactions)")  # Feedback if no activity recorded
else:
    for i, t in enumerate(selected.transactions, 1):
        # Display transaction number, timestamp, type, amount, balance after, and optional note
        print(
            f"{i:02d}. {t.timestamp} | {t.kind:<8} | amt={t.amount:.2f} | bal={t.balance_after:.2f}"
            + (f" | {t.note}" if t.note else "")
        )

elif choice == "8":
    # Persist all accounts and transactions to disk
    bank.save(DATA_FILE)
    print("Saved.")

elif choice == "9":
    # Exit cleanly and stop the loop
    print("Goodbye!")
    break

else:
    # Catch any invalid menu option
    print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
