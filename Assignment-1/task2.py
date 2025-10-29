def reverse_string(input_string):
    """
    Function to reverse a string
    Args:
        input_string (str): The input string to be reversed
    Returns:
        str: The reversed string
    """
    return input_string[::-1]

# Example usage
if __name__ == "__main__":
    # Prompt the user for input
    user_input = input("Enter a string to reverse: ")
    reversed_string = reverse_string(user_input)
    print(f"Original string: {user_input}")
    print(f"Reversed string: {reversed_string}")
