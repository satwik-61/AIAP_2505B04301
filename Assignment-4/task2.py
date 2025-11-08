"""Simple script to convert centimeters to inches.

It prompts the user for a length in centimeters (manual input) and prints the
equivalent length in inches using the conversion 1 cm = 0.393701 inch.
"""
CM_TO_INCH = 0.393701


def cm_to_inches(centimeters: float) -> float:
	"""Convert centimeters to inches using the factor 0.393701.

	Raises:
		ValueError: If centimeters is negative.
	"""
	if centimeters < 0:
		raise ValueError("Length cannot be negative.")
	return centimeters * CM_TO_INCH


def prompt_and_convert() -> None:
	"""Prompt for centimeters, validate input, and print inches result."""
	raw = input("Enter length in centimeters (e.g., 10.5): ").strip()
	if raw == "":
		print("No input provided. Please enter a numeric length next time.")
		return
	try:
		centimeters = float(raw)
		inches = cm_to_inches(centimeters)
	except ValueError as exc:
		print(f"Invalid input: {raw!r}. {exc}")
		return
	print(f"{centimeters} cm = {inches:.6f} inches")


if __name__ == "__main__":
	prompt_and_convert()


