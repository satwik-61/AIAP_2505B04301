class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
    
    def display_info(self):
        """Display student information"""
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Example usage
if __name__ == "__main__":
    student = Student("John Doe", 20, "S12345")
    student.display_info()

