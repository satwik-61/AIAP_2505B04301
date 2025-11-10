def print_multiples_while():
    """Print the first 10 multiples of a number using while loop"""
    n = int(input("Enter a number: "))
    i = 1
    while i <= 10:
        print(f"{n} × {i} = {n * i}")
        i += 1


# Example usage
if __name__ == "__main__":
    print_multiples_while()

