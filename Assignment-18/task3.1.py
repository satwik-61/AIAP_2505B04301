def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    # Test cases
    print(f"Factorial of 0: {factorial(0)}")
    print(f"Factorial of 1: {factorial(1)}")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Factorial of 10: {factorial(10)}")
