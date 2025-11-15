from collections.abc import Iterable
from typing import Tuple

def sum_even_odd(numbers: Iterable[int]) -> Tuple[int, int]:
    """Return the total of even and odd numbers from an iterable.

    Goes through each integer, adds up the even ones and the odd ones
    separately, and returns both totals.

    Args:
        numbers (Iterable[int]): Iterable of integers.

    Returns:
        Tuple[int, int]: (sum_of_evens, sum_of_odds)

    Raises:
        TypeError: If any item in the iterable is not an integer.
    """
    even_sum = 0
    odd_sum = 0

    for value in numbers:
        if not isinstance(value, int):
            raise TypeError(f"All elements must be integers, but got {type(value).__name__!r}.")
        if value % 2 == 0:
            even_sum += value
        else:
            odd_sum += value

    return even_sum, odd_sum

if __name__ == "__main__":
    sample_values = [10, 21, 32, 43, 0, -5]
    even_total, odd_total = sum_even_odd(sample_values)
    print(f"Input values: {sample_values}")
    print(f"Even sum: {even_total}, Odd sum: {odd_total}")

