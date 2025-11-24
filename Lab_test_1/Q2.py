"""Small utility to get the larger of two numbers.

This module defines a single function `largest` which returns the
larger of two numeric values. A short example run is provided when
the module is executed as a script.
"""

from typing import Union

Number = Union[int, float]


def largest(a: Number, b: Number) -> Number:
	"""Return the larger of two numbers a and b.

	If the values are equal, this function returns that same value.

	Args:
		a: First number (int or float).
		b: Second number (int or float).

	Returns:
		The larger of `a` and `b`.
	"""

	# Use a simple comparison; this is clear and efficient for two values.
	if a > b:
		return a
	return b


if __name__ == "__main__":
	# Example usage / quick smoke test when run directly.
	result = largest(10, 7)
	print("Largest number is:", result)

