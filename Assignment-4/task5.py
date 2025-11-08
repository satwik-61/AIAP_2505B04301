"""Utilities to count the number of lines in a text file by path.

Behavior:
- Returns the number of newline-terminated lines in the file (universal newlines)
- Empty file -> 0
- Missing path -> raises FileNotFoundError
"""


def count_lines(file_path: str) -> int:
	"""Return the number of lines in the file at `file_path`.

	Opens in text mode with UTF-8 and ignores decode errors so that files with
	mixed encodings can still be counted. Raises FileNotFoundError if the path
	does not exist.
	"""
	with open(file_path, mode="r", encoding="utf-8", errors="ignore") as f:
		return sum(1 for _ in f)

def prompt_and_count() -> None:
	"""Prompt the user for a file path and print the number of lines."""
	path = input("Enter file path: ").strip()
	if path == "":
		print("No input provided. Please enter a file path next time.")
		return
	try:
		count = count_lines(path)
	except FileNotFoundError:
		print("File not found. Please check the path and try again.")
		return
	except OSError as exc:
		print(f"Could not read file: {exc}")
		return
	print(f"Number of lines: {count}")

if __name__ == "__main__":
	prompt_and_count()


