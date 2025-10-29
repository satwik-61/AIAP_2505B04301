def sum_of_squares():
    """
    This function calculates the sum of squares of numbers input by the user.
    It allows multiple numbers to be entered and handles input validation.
    """
    try:
        # Get the count of numbers from user
        n = int(input("Enter how many numbers you want to calculate: "))
        
        # Validate if the count is positive
        if n <= 0:
            raise ValueError("Please enter a positive number.")
        
        numbers = []
        # Get numbers from user
        for i in range(n):
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
        
        # Calculate sum of squares
        squares = [num ** 2 for num in numbers]
        sum_squares = sum(squares)
        
        # Display results
        print("\nResults:")
        print("--------")
        for i, (num, square) in enumerate(zip(numbers, squares)):
            print(f"{num}² = {square}")
        print(f"Sum of squares = {sum_squares}")
        
        return sum_squares
    
    except ValueError as e:
        if "could not convert" in str(e):
            print("Error: Please enter valid numbers only.")
        else:
            print(f"Error: {str(e)}")
        return None

# Only run if this is the main program
if __name__ == "__main__":
    print("Sum of Squares Calculator")
    print("------------------------")
    
    while True:
        sum_of_squares()
        choice = input("\nCalculate again? (yes/no): ").lower()
        if choice != 'yes':
            print("Goodbye!")
            break
