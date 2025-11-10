def classify_age(age):
    """Classify age groups using nested if-elif-else"""
    if age < 0:
        print("Invalid age")
    elif age < 13:
        print("Child")
    elif age < 18:
        print("Teenager")
    elif age < 65:
        if age < 30:
            print("Young Adult")
        elif age < 50:
            print("Adult")
        else:
            print("Middle-aged Adult")
    else:
        if age < 80:
            print("Senior")
        else:
            print("Elderly")


# Example usage
if __name__ == "__main__":
    age = int(input("Enter age: "))
    classify_age(age)

