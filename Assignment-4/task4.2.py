"""Count the number of vowels in a string.

Examples:
- Numbers = 2 vowels (u, e)
- Perfume = 3 vowels (e, u, e)
- Calendar = 3 vowels (a, e, a)
- Vinayaka = 4 vowels (i, a, a, a)
"""

VOWELS = set("aeiouAEIOU")


def count_vowels(text: str) -> int:
	"""Return the count of vowels (a, e, i, o, u) in the given text.
	
	Args:
		text: The string to count vowels in.
		
	Returns:
		The number of vowels found in the string.
	"""
	return sum(1 for ch in text if ch in VOWELS)


def prompt_and_count() -> None:
	"""Prompt the user for a string and print the number of vowels found."""
	text = input("Enter a string: ").strip()
	if text == "":
		print("No input provided. Please enter a string next time.")
		return
	count = count_vowels(text)
	print(f"Number of vowels: {count}")


if __name__ == "__main__":
	prompt_and_count()

