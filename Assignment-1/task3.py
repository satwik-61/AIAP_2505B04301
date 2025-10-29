"""
task3.py

Contains both recursive and iterative implementations of factorial
and a small CLI to test them.
"""

def factorial_recursive(n):
    """Compute factorial of n recursively.

    Args:
        n (int): non-negative integer

    Returns:
        int: n!

    Raises:
        TypeError: if n is not an int
        ValueError: if n is negative
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """Compute factorial of n using an iterative loop.

    Args:
        n (int): non-negative integer

    Returns:
        int: n!

    Raises:
        TypeError: if n is not an int
        ValueError: if n is negative
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    # Simple CLI: prompt user for an integer and show both results
    try:
        user_input = input("Enter a non-negative integer to compute factorial: ")
        n = int(user_input)
        rec = factorial_recursive(n)
        it = factorial_iterative(n)
        print(f"factorial_recursive({n}) = {rec}")
        print(f"factorial_iterative({n}) = {it}")
        # quick self-check
        if rec != it:
            print("Warning: recursive and iterative results differ")
    except Exception as e:
        print("Error:", e)
