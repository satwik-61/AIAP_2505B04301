def sum_to_n(n):
    """Calculate the sum of first n numbers"""
    if n < 0:
        return 0
    return n * (n + 1) // 2

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Sum of first {n} numbers (formula): {sum_to_n(n)}")

