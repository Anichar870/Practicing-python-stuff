def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def display_menu():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def calculator():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":  # Addition
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {add(x, y)}")
        
        elif choice == "2":  # Subtraction
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {subtract(x, y)}")
        
        elif choice == "3":  # Multiplication
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {multiply(x, y)}")
        
        elif choice == "4":  # Division
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {divide(x, y)}")
        
        elif choice == "5":  # Exit
            print("Exiting calculator. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    calculator()
