def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    finally:
        print("Execution completed.")

divide(10, 2)  # Normal case
divide(5, 0)   # Error case
