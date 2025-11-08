"""Count the number of vowels in a string and print the result."""

VOWELS = set("aeiouAEIOU")


def count_vowels(text: str) -> int:
	"""Return the count of vowels (a, e, i, o, u) in the given text."""
	return sum(1 for ch in text if ch in VOWELS)


def prompt_and_count() -> None:
	"""Prompt the user for a string and print the number of vowels found."""
	text = input("Enter a string: ")
	count = count_vowels(text)
	print(f"Number of vowels: {count}")


if __name__ == "__main__":
	prompt_and_count()


