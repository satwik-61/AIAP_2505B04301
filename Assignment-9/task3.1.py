from typing import Iterable

def add(values: Iterable[float]) -> float:
    """
    Add up all numbers in the given iterable.
    This function goes through each number and returns the total sum.
    Parameters
    values : Iterable[float]
        A collection of numbers (like a list or tuple) to be added.

    Returns
    float
        The total sum of all the numbers.
    """
    total = 0.0
    for number in values:
        total += number
    return total

def subtract(minuend: float, subtrahend: float) -> float:
    """
    Subtract one number from another.
    Parameters
    minuend : float
        The number from which another number is subtracted.
    subtrahend : float
        The number to subtract from the minuend.

    Returns
    float
        The result of the subtraction (`minuend - subtrahend`).
    """
    return minuend - subtrahend

def multiply(values: Iterable[float]) -> float:
    """
    Multiply all numbers in the given iterable.
    Goes through each number and multiplies them together.
    Parameters
    values : Iterable[float]
        A collection of numbers (like a list or tuple) to multiply.

    Returns
    float
        The product of all the numbers.
    """
    product = 1.0
    for number in values:
        product *= number
    return product

def divide(dividend: float, divisor: float) -> float:
    """
    Divide one number by another.
    Parameters
    dividend : float
        The number to be divided.
    divisor : float
        The number to divide by. Must not be zero.

    Returns
    float
        The result of the division (`dividend / divisor`).

    Raises
    ZeroDivisionError
        If `divisor` is zero.
    """
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return dividend / divisor


if __name__ == "__main__":
    nums = [10, 5, 3]
    print(f"Add {nums}: {add(nums)}")
    print(f"Subtract 10 - 5: {subtract(10, 5)}")
    print(f"Multiply {nums}: {multiply(nums)}")
    print(f"Divide 10 / 2: {divide(10, 2)}")

