import sys
import os

# Create output.txt path in the same folder as this script
output_file = os.path.join(os.path.dirname(__file__), 'output.txt')

# Redirect all print() output to output.txt
sys.stdout = open(output_file, 'w')

# ----------------- Classes -----------------
class InsufficientFundsError(Exception):
    """Exception raised when withdrawal amount exceeds account balance."""
    pass

class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Cannot withdraw ₹{amount}. Available balance: ₹{self.balance}")
        self.balance -= amount
        print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
    
    def check_balance(self):
        print(f"Current balance for account {self.account_number}: ₹{self.balance}")

# ----------------- Example usage -----------------
    try:
        account = BankAccount("12345", "Sakshi", 1000)
        print(account.check_balance())
        print(account.deposit(500))
        print(account.withdraw(300))
        print(account.withdraw(2000))  # Will raise InsufficientFundsError
    except InsufficientFundsError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")

# Close the file so output is saved
sys.stdout.close()
