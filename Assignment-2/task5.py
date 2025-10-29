def calculate_odd_even_sums():
    """
    This function takes user input for numbers and calculates 
    the sum of odd and even numbers separately.
    """
    try:
        # Get the count of numbers from user
        n = int(input("How many numbers do you want to enter? "))
        
        if n <= 0:
            raise ValueError("Please enter a positive number.")
        
        # Initialize lists for odd and even numbers
        numbers = []
        odd_numbers = []
        even_numbers = []
        
        # Get numbers from user
        for i in range(n):
            num = int(input(f"Enter number {i+1}: "))
            numbers.append(num)
            
            # Categorize numbers as odd or even
            if num % 2 == 0:
                even_numbers.append(num)
            else:
                odd_numbers.append(num)
        
        # Calculate sums
        sum_odd = sum(odd_numbers)
        sum_even = sum(even_numbers)
        
        # Display results
        print("\nResults:")
        print("--------")
        print(f"All numbers entered: {numbers}")
        print(f"\nEven numbers: {even_numbers}")
        print(f"Sum of even numbers: {sum_even}")
        print(f"\nOdd numbers: {odd_numbers}")
        print(f"Sum of odd numbers: {sum_odd}")
        
        return sum_odd, sum_even
        
    except ValueError as e:
        if "invalid literal" in str(e):
            print("Error: Please enter whole numbers only.")
        else:
            print(f"Error: {str(e)}")
        return None, None

# Main program
if __name__ == "__main__":
    print("Odd and Even Number Sum Calculator")
    print("--------------------------------")
    
    while True:
        calculate_odd_even_sums()
        choice = input("\nCalculate again? (yes/no): ").lower()
        if choice != 'yes':
            print("Goodbye!")
            break
