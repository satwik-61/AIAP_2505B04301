from collections.abc import Iterable
from typing import Tuple

def sum_even_odd(numbers: Iterable[int]) -> Tuple[int, int]:
    """Return the sums of even and odd integers from the provided iterable.

    Args:
        numbers (Iterable[int]): A sequence of integers to analyze.

    Returns:
        Tuple[int, int]: Pair of totals where index 0 is the sum of even values
        and index 1 is the sum of odd values.

    Raises:
        TypeError: If any element in `numbers` is not an integer.
    """
    even_sum = 0
    odd_sum = 0

    for value in numbers:
        if not isinstance(value, int):
            raise TypeError(f"Expected integers only, but received {type(value).__name__!r}.")
        if value % 2 == 0:
            even_sum += value
        else:
            odd_sum += value

    return even_sum, odd_sum

if __name__ == "__main__":
    sample_values = [4, 7, 12, -3, 0, 5]
    even_total, odd_total = sum_even_odd(sample_values)
    print(f"Input values: {sample_values}")
    print(f"Even sum: {even_total}, Odd sum: {odd_total}")
