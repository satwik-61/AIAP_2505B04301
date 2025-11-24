"""Q1: Stack implementation with interactive CLI

Provides a Stack class with push, pop, peek, is_empty and size methods.
Run without arguments for an interactive prompt. Use `--test` to run a quick demo and exit.
"""

import argparse
from typing import Any, List


class Stack:
	"""Simple stack implementation using Python list as underlying storage.

	Methods:
	- push(value): push a value onto the stack
	- pop(): remove and return the top value (raises IndexError on empty)
	- peek(): return the top value without removing (raises IndexError on empty)
	- is_empty(): return True if stack empty
	- size(): return number of elements
	"""

	def __init__(self) -> None:
		self._items: List[Any] = []

	def push(self, value: Any) -> None:
		"""Push value onto the stack."""
		self._items.append(value)

	def pop(self) -> Any:
		"""Pop and return the top value. Raises IndexError if empty."""
		if self.is_empty():
			raise IndexError("pop from empty stack")
		return self._items.pop()

	def peek(self) -> Any:
		"""Return the top value without removing it. Raises IndexError if empty."""
		if self.is_empty():
			raise IndexError("peek from empty stack")
		return self._items[-1]

	def is_empty(self) -> bool:
		return len(self._items) == 0

	def size(self) -> int:
		return len(self._items)

	def __str__(self) -> str:
		# Show stack with top on the right
		return "Stack(bottom -> top): " + str(self._items)


def _parse_value(s: str) -> Any:
	"""Try to parse input string as int or float; otherwise return as string."""
	s = s.strip()
	if s == "":
		return ""
	# try int
	try:
		return int(s)
	except ValueError:
		pass
	# try float
	try:
		return float(s)
	except ValueError:
		pass
	return s


def interactive_loop() -> None:
	s = Stack()
	menu = (
		"\nChoose an action:\n"
		"1) Push\n"
		"2) Pop\n"
		"3) Peek\n"
		"4) Display stack\n"
		"5) Size\n"
		"6) Exit\n"
		"Enter choice (1-6): "
	)

	while True:
		try:
			choice = input(menu).strip()
		except (EOFError, KeyboardInterrupt):
			print("\nExiting.")
			break

		if choice == "1":
			val = input("Value to push: ")
			parsed = _parse_value(val)
			s.push(parsed)
			print(f"Pushed: {parsed}")

		elif choice == "2":
			try:
				popped = s.pop()
				print(f"Popped: {popped}")
			except IndexError as e:
				print(f"Error: {e}")

		elif choice == "3":
			try:
				top = s.peek()
				print(f"Top: {top}")
			except IndexError as e:
				print(f"Error: {e}")

		elif choice == "4":
			print(s)

		elif choice == "5":
			print(f"Size: {s.size()}")

		elif choice == "6":
			print("Goodbye.")
			break

		else:
			print("Invalid option, please enter a number 1-6.")


def run_test_demo() -> None:
	"""Run a quick non-interactive demo to verify functionality."""
	print("Running test demo...")
	s = Stack()
	print("Initial empty?", s.is_empty())
	s.push(10)
	s.push(20)
	s.push("hello")
	print(s)
	print("Size after 3 pushes:", s.size())
	print("Peek ->", s.peek())
	print("Pop ->", s.pop())
	print("Peek after pop ->", s.peek())
	print("Final stack:", s)


def main() -> None:
	parser = argparse.ArgumentParser(description="Stack CLI (Q1)")
	parser.add_argument("--test", action="store_true", help="run test/demo and exit")
	args = parser.parse_args()

	if args.test:
		run_test_demo()
	else:
		interactive_loop()


if __name__ == "__main__":
	main()

