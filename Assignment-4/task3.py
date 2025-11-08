"""Parse names written as "Last, First" and print components.
Examples:
Input:  "Chittimalla, Pujitha"  -> First name: Chittimalla | Last name: Pujitha
Input:  "Chittimalla, Rajasree" -> First name: Chittimalla | Last name: Rajasree
"""
def parse_last_first(full_name: str) -> tuple[str, str]:
	"""Return (first_name_label, last_name_label) from a "Last, First" string.
	The labels follow the user's requested mapping:
	- "First name" is the text BEFORE the comma (family/surname)
	- "Last name" is the text AFTER the comma (given name)
	"""
	parts = full_name.split(",", 1)
	if len(parts) != 2:
		raise ValueError("Expected format: 'Last, First'")
	last_part, first_part = parts[0].strip(), parts[1].strip()
	if not last_part or not first_part:
		raise ValueError("Both last and first parts must be non-empty")
	first_name_label = last_part
	last_name_label = first_part
	return first_name_label, last_name_label

def prompt_and_print() -> None:
	"""Prompt the user for a name in "Last, First" format and print labels."""
	raw = input("Enter full name in 'Last, First' format: ").strip()
	if raw == "":
		print("No input provided. Please enter a name next time.")
		return
	try:
		first_name_label, last_name_label = parse_last_first(raw)
	except ValueError as exc:
		print(f"Invalid input: {exc}")
		return
	print(f"First name : {first_name_label}")
	print(f"Last name: {last_name_label}")

if __name__ == "__main__":
	prompt_and_print()


