class BankAccount:
    """
    A simple BankAccount class that handles basic banking operations
    like deposit, withdraw and checking balance.
    """
    
    def __init__(self):
        """Initialize the account with zero balance"""
        self.balance = 0
    
    def deposit(self, amount):
        """
        Deposit money into the account
        Args:
            amount (float): Amount to deposit
        Returns:
            str: Success message
        """
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f} successfully"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """
        Withdraw money from the account
        Args:
            amount (float): Amount to withdraw
        Returns:
            str: Success or error message
        """
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount:.2f} successfully"
        return "Insufficient balance or invalid amount"
    
    def get_balance(self):
        """
        Check current balance
        Returns:
            float: Current balance
        """
        return self.balance

# Create a bank account instance
account = BankAccount()

# Main program loop
while True:
    print("\n=== Banking Menu ===")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == '1':
        amount = float(input("Enter deposit amount: $"))
        print(account.deposit(amount))
    
    elif choice == '2':
        amount = float(input("Enter withdrawal amount: $"))
        print(account.withdraw(amount))
    
    elif choice == '3':
        print(f"Current balance: ${account.get_balance():.2f}")
    
    elif choice == '4':
        print("Thank you for banking with us!")
        break
    
    else:
        print("Invalid choice. Please try again.")
