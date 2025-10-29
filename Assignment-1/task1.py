import math
import sys

def is_prime(n: int) -> bool:
	"""Return True if n is prime, False otherwise.

	Works for n >= 0. Uses trial division up to sqrt(n).
	"""
	if n < 2:
		return False
	if n in (2, 3):
		return True
	if n % 2 == 0:
		return False
	limit = int(math.isqrt(n)) + 1
	for i in range(3, limit, 2):
		if n % i == 0:
			return False
	return True

def main():
	try:
		s = input("Enter an integer: ").strip()
		n = int(s)
	except ValueError:
		print("Invalid input. Please enter a valid integer.", file=sys.stderr)
		sys.exit(1)

	if is_prime(n):
		print(f"{n} is a prime number.")
	else:
		print(f"{n} is not a prime number.")

if __name__ == "__main__":
	main()

