def classify_age_match(age):
    """Classify age groups using match-case statement"""
    match True:
        case _ if age < 0:
            print("Invalid age")
        case _ if age < 13:
            print("Child")
        case _ if age < 18:
            print("Teenager")
        case _ if age < 30:
            print("Young Adult")
        case _ if age < 50:
            print("Adult")
        case _ if age < 65:
            print("Middle-aged Adult")
        case _ if age < 80:
            print("Senior")
        case _:
            print("Elderly")

def classify_age_ternary(age):
    """Classify age groups using ternary operators"""
    result = "Invalid age" if age < 0 else \
             "Child" if age < 13 else \
             "Teenager" if age < 18 else \
             "Young Adult" if age < 30 else \
             "Adult" if age < 50 else \
             "Middle-aged Adult" if age < 65 else \
             "Senior" if age < 80 else \
             "Elderly"
    print(result)

def classify_age_logical(age):
    """Classify age groups using logical operators"""
    if age < 0:
        print("Invalid age")
    elif 0 <= age < 13:
        print("Child")
    elif 13 <= age < 18:
        print("Teenager")
    elif 18 <= age < 30 and age >= 18:
        print("Young Adult")
    elif age >= 30 and age < 50:
        print("Adult")
    elif age >= 50 and age < 65:
        print("Middle-aged Adult")
    elif age >= 65 and age < 80:
        print("Senior")
    else:
        print("Elderly")

# Example usage
if __name__ == "__main__":
    age = int(input("Enter age: "))
    print("\nUsing match-case:")
    classify_age_match(age)
    print("\nUsing ternary operators:")
    classify_age_ternary(age)
    print("\nUsing logical operators:")
    classify_age_logical(age)