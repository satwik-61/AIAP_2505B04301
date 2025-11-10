def print_multiples(n):
    """Print the first 10 multiples of a number"""
    for i in range(1, 11):
        print(f"{n} × {i} = {n * i}")


# Example usage
if __name__ == "__main__":
    print_multiples(5)

