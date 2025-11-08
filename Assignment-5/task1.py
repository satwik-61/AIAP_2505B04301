import json
import hashlib
import os

# File to store user data
USERS_FILE = "users.json"

def get_password_input(prompt="Enter password: "):
    """Get password input - uses regular input for IDE compatibility"""
    # Using regular input() to ensure it works in all environments (IDEs, terminals, etc.)
    # Note: Password will be visible when typing
    # This ensures compatibility with Windows PowerShell and IDE consoles
    password = input(prompt)
    return password

def load_users():
    """Load users from JSON file"""
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_users(users):
    """Save users to JSON file"""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    """Register a new user"""
    print("\n=== User Registration ===")
    username = input("Enter username: ").strip()
    
    if not username:
        print("Username cannot be empty!")
        return
    
    users = load_users()
    
    if username in users:
        print("Username already exists! Please choose a different username.")
        return
    
    password = get_password_input("Enter password: ")
    if len(password) < 6:
        print("Password must be at least 6 characters long!")
        return
    
    confirm_password = get_password_input("Confirm password: ")
    
    if password != confirm_password:
        print("Passwords do not match!")
        return
    
    # Hash the password before storing
    hashed_password = hash_password(password)
    
    # Store user data
    users[username] = {
        "password": hashed_password,
        "registered_date": ""  # Can be enhanced with datetime
    }
    
    save_users(users)
    print(f"\n✓ User '{username}' registered successfully!")

def login_user():
    """Login an existing user"""
    print("\n=== User Login ===")
    username = input("Enter username: ").strip()
    password = get_password_input("Enter password: ")
    
    users = load_users()
    
    if username not in users:
        print("Invalid username or password!")
        return False
    
    # Hash the entered password and compare with stored hash
    hashed_password = hash_password(password)
    
    if users[username]["password"] == hashed_password:
        print(f"\n✓ Login successful! Welcome, {username}!")
        return True
    else:
        print("Invalid username or password!")
        return False

def change_password():
    """Change password for logged-in user"""
    print("\n=== Change Password ===")
    username = input("Enter username: ").strip()
    users = load_users()
    
    if username not in users:
        print("User not found!")
        return
    
    current_password = get_password_input("Enter current password: ")
    hashed_current = hash_password(current_password)
    
    if users[username]["password"] != hashed_current:
        print("Current password is incorrect!")
        return
    
    new_password = get_password_input("Enter new password: ")
    if len(new_password) < 6:
        print("Password must be at least 6 characters long!")
        return
    
    confirm_password = get_password_input("Confirm new password: ")
    
    if new_password != confirm_password:
        print("Passwords do not match!")
        return
    
    users[username]["password"] = hash_password(new_password)
    save_users(users)
    print("\n✓ Password changed successfully!")

def delete_user():
    """Delete a user account"""
    print("\n=== Delete User Account ===")
    username = input("Enter username to delete: ").strip()
    users = load_users()
    
    if username not in users:
        print("User not found!")
        return
    
    confirm = input(f"Are you sure you want to delete user '{username}'? (yes/no): ").strip().lower()
    
    if confirm == 'yes':
        password = get_password_input("Enter password to confirm: ")
        hashed_password = hash_password(password)
        
        if users[username]["password"] == hashed_password:
            del users[username]
            save_users(users)
            print(f"\n✓ User '{username}' deleted successfully!")
        else:
            print("Incorrect password! User deletion cancelled.")
    else:
        print("User deletion cancelled.")

def list_users():
    """List all registered users (admin function)"""
    print("\n=== Registered Users ===")
    users = load_users()
    
    if not users:
        print("No users registered yet.")
        return
    
    print(f"\nTotal users: {len(users)}")
    print("\nUsernames:")
    for username in users.keys():
        print(f"  - {username}")

def main_menu():
    """Display main menu and handle user choices"""
    while True:
        print("\n" + "="*40)
        print("    LOGIN SYSTEM MENU")
        print("="*40)
        print("1. Register")
        print("2. Login")
        print("3. Change Password")
        print("4. Delete User")
        print("5. List Users")
        print("6. Exit")
        print("="*40)
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            change_password()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            list_users()
        elif choice == '6':
            print("\nThank you for using the Login System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    print("Welcome to the Login System!")
    main_menu()