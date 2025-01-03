# Multiplication Table Generator

# Get input from the user
number = int(input("Enter a number to generate its multiplication table: "))
limit = int(input("Enter the limit of the table: "))

print(f"\nMultiplication Table for {number} up to {limit}:\n")

# Loop to generate the table
for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}")

print("\nThank you for using the Multiplication Table Generator!")
