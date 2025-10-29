def check_palindrome():
    # Get input from user
    user_input = input("Enter a string or number to check if it's a palindrome: ")
    
    # Convert to string and clean the input (remove spaces and special characters)
    # Convert to lowercase to make comparison case-insensitive
    cleaned_input = ''.join(char.lower() for char in str(user_input) if char.isalnum())
    
    # Check if the cleaned input is equal to its reverse
    is_palindrome = cleaned_input == cleaned_input[::-1]
    
    # Print the result
    if is_palindrome:
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is not a palindrome.")
    
    return is_palindrome

# Run the function if the script is run directly
if __name__ == "__main__":
    while True:
        check_palindrome()
        
        # Ask if user wants to check another palindrome
        another = input("\nDo you want to check another palindrome? (yes/no): ").lower()
        if another != 'yes':
            print("Goodbye")
            break
        
