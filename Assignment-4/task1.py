"""Simple script to check whether a given year is a leap year.

It prompts the user for a year (manual input) and prints the result.
"""
def is_leap_year(year: int) -> bool:
	"""Return True if `year` is a leap year (Gregorian rules), else False.

	Rules:
	- Every year divisible by 4 is a leap year,
	  except years divisible by 100 which are not leap years,
	  unless they are also divisible by 400.
	"""
	return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def prompt_and_check() -> None:
	"""Prompt the user for a year, validate input, and print whether it's a leap year.

	Accepts integer input only. Prints a helpful message for invalid input.
	"""
	raw = input("Enter a year (e.g., 2024): ").strip()
	if raw == "":
		print("No input provided. Please enter a year next time.")
		return
	try:
		year = int(raw)
	except ValueError:
		print(f"Invalid input: {raw!r}. Please enter a whole number (e.g., 2024).")
		return

	if is_leap_year(year):
		print(f"{year} is a leap year.")
	else:
		print(f"{year} is NOT a leap year.")


if __name__ == "__main__":
	prompt_and_check()

