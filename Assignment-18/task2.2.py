def check_number(num):
    if num > 0:
        print(f"{num} is a positive number.")
    elif num < 0:
        print(f"{num} is a negative number.")
    else:
        print(f"{num} is zero.")


if __name__ == "__main__":
    check_number(5)
    check_number(-3)
    check_number(0)
