# Function to calculate the nth Fibonacci number using recursion
def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.  
    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
    Position:          0, 1, 2, 3, 4, 5, 6,  7,  8,  9, 10, ...
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1
    """
    # Base case 1: If n is 0, return 0
    # Position 0 corresponds to the first number in the sequence: 0
    if n == 0:
        return 0   
    # Base case 2: If n is 1, return 1
    # Position 1 corresponds to the second number in the sequence: 1
    if n == 1:
        return 1
    # Recursive case: For n > 1, calculate F(n) = F(n-1) + F(n-2)
    # This breaks down the problem into smaller subproblems:
    # - fibonacci_recursive(n-1) calculates the Fibonacci number at position (n-1)
    # - fibonacci_recursive(n-2) calculates the Fibonacci number at position (n-2)
    # - Adding them gives us the Fibonacci number at position n
    # The recursion continues until it reaches the base cases (n=0 or n=1)
    # Example: F(5) = F(4) + F(3) = (F(3)+F(2)) + (F(2)+F(1)) = ... = 5
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
# Main program to get user input and calculate Fibonacci number
if __name__ == "__main__":
    # Get user input for the position in Fibonacci sequence
    try:
        # Prompt user to enter a non-negative integer
        n = int(input("Enter the position (n) to calculate nth Fibonacci number: "))       
        # Validate input: check if n is negative
        if n < 0:
            print("Error: Please enter a non-negative integer.")
        else:
            # Calculate the nth Fibonacci number using recursion
            result = fibonacci_recursive(n)            
            # Display the result with position information
            # Position 0 = first number (0), Position 1 = second number (1), etc.
            print(f"F({n}) = {result}")
            print(f"The Fibonacci number at position {n} is: {result}")
            
            # Show a few examples for clarity
            if n <= 10:
                print(f"\nFirst few Fibonacci numbers for reference:")
                for i in range(min(n + 3, 11)):
                    print(f"  F({i}) = {fibonacci_recursive(i)}", end="")
                    if i == n:
                        print(" <-- Your answer")
                    else:
                        print()   
    except ValueError:
        # Handle error if user enters non-integer value
        print("Error: Please enter a valid integer.")
