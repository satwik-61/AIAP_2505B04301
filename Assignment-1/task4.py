"""
task4.py

Prompt the user to enter numbers (space- or comma-separated), parse them,
and print the largest number.
"""

from typing import Iterable, Union, List


def find_largest(numbers: Iterable[Union[int, float]]) -> Union[int, float]:
	"""Return the largest number from an iterable of numbers.

	Raises ValueError if the iterable is empty, TypeError if non-numeric
	elements are encountered.
	"""
	iterator = iter(numbers)
	try:
		largest = next(iterator)
	except StopIteration:
		raise ValueError("Empty iterable")

	if not isinstance(largest, (int, float)):
		raise TypeError("All elements must be int or float")

	for x in iterator:
		if not isinstance(x, (int, float)):
			raise TypeError("All elements must be int or float")
		if x > largest:
			largest = x
	return largest


def parse_numbers(s: str) -> List[Union[int, float]]:
	"""Parse a string of numbers separated by spaces and/or commas.

	Examples accepted: "1 2 3", "1,2,3", "1, 2 3"
	Raises ValueError for invalid tokens.
	"""
	s = s.strip()
	if not s:
		return []

	parts = [p for chunk in s.split(',') for p in chunk.split()]
	nums: List[Union[int, float]] = []
	for p in parts:
		try:
			# Try int first to preserve integer types where possible
			if p.count('.') == 0:
				val = int(p)
			else:
				val = float(p)
		except ValueError:
			# Final attempt: maybe it's a float with locale-like formatting
			try:
				val = float(p)
			except ValueError:
				raise ValueError(f"Invalid number: '{p}'")
		nums.append(val)
	return nums


if __name__ == "__main__":
	try:
		user_input = input("Enter numbers separated by spaces or commas: ")
		numbers = parse_numbers(user_input)
		if not numbers:
			print("No numbers provided.")
		else:
			largest = find_largest(numbers)
			print(f"The largest number is: {largest}")
	except Exception as e:
		print("Error:", e)

