from typing import Iterable

def add(values: Iterable[float]) -> float:
    """Return the arithmetic sum of all numbers in `values`.

    Parameters
    ----------
    values : Iterable[float]
        Numbers to be added together.

    Returns
    -------
    float
        Total sum of the provided numbers.
    """
    total = 0.0
    for number in values:
        total += number
    return total

def subtract(minuend: float, subtrahend: float) -> float:
    """Return the result of subtracting `subtrahend` from `minuend`.

    Parameters
    ----------
    minuend : float
        Value from which the second number is subtracted.
    subtrahend : float
        Value to subtract from the first number.

    Returns
    -------
    float
        Difference of the two numbers.
    """
    return minuend - subtrahend

def multiply(values: Iterable[float]) -> float:
    """Return the product of all numbers in `values`.

    Parameters
    ----------
    values : Iterable[float]
        Numbers to multiply together.

    Returns
    -------
    float
        Product of the provided numbers.
    """
    product = 1.0
    for number in values:
        product *= number
    return product

def divide(dividend: float, divisor: float) -> float:
    """Return the quotient of dividing `dividend` by `divisor`.

    Parameters
    ----------
    dividend : float
        Numerator of the division.
    divisor : float
        Denominator of the division.

    Returns
    -------
    float
        Resulting quotient.

    Raises
    ------
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

