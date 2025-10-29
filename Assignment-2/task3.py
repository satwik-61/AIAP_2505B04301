import math

def calculate_area():
    """
    This function provides a menu-driven interface to calculate areas of different shapes.
    Supported shapes: circle, rectangle, triangle, and square.
    """
    # Print the menu of available shapes
    print("\nShape Area Calculator")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")
    
    try:
        # Get user's choice of shape
        choice = int(input("\nEnter the number of the shape (1-4): "))
        
        # Calculate area based on the selected shape
        if choice == 1:  # Circle
            radius = float(input("Enter the radius of the circle: "))
            if radius < 0:
                raise ValueError("Radius cannot be negative")
            area = math.pi * radius ** 2
            print(f"\nArea of the circle with radius {radius} is: {area:.2f} square units")
            
        elif choice == 2:  # Rectangle
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            if length < 0 or width < 0:
                raise ValueError("Length and width cannot be negative")
            area = length * width
            print(f"\nArea of the rectangle with length {length} and width {width} is: {area:.2f} square units")
            
        elif choice == 3:  # Triangle
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            if base < 0 or height < 0:
                raise ValueError("Base and height cannot be negative")
            area = 0.5 * base * height
            print(f"\nArea of the triangle with base {base} and height {height} is: {area:.2f} square units")
            
        elif choice == 4:  # Square
            side = float(input("Enter the side length of the square: "))
            if side < 0:
                raise ValueError("Side length cannot be negative")
            area = side ** 2
            print(f"\nArea of the square with side {side} is: {area:.2f} square units")
            
        else:
            print("Invalid choice! Please select a number between 1 and 4.")
            
    except ValueError as e:
        if str(e).startswith("could not convert"):
            print("Error: Please enter numeric values only.")
        else:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    while True:
        calculate_area()
        another = input("\nDo you want to calculate another area? (yes/no): ").lower()
        if another != 'yes':
            print("Thank you for using the Shape Area Calculator!")
            break
