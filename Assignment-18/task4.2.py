def print_students(students):
    print("Student Names:")
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student}")


# Test with sample student names
student_list = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
print_students(student_list)
