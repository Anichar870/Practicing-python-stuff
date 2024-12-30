import json
import os

EXPENSE_FILE = "expenses.json"

def initialize_expenses():
    """Initialize the expense file if it doesn't exist."""
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "w") as file:
            json.dump([], file)

def load_expenses():
    """Load expenses from the file."""
    with open(EXPENSE_FILE, "r") as file:
        return json.load(file)

def save_expenses(expenses):
    """Save expenses to the file."""
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    """Add a new expense."""
    try:
        category = input("Enter the expense category (e.g., Food, Rent): ")
        amount = float(input("Enter the amount: "))
        description = input("Enter a brief description (optional): ")
        
        expense = {
            "category": category,
            "amount": amount,
            "description": description
        }
        expenses = load_expenses()
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_expenses():
    """View all expenses."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet!")
        return
    
    print("\nRecorded Expenses:")
    total = 0
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['category']} - ${expense['amount']:.2f} ({expense['description']})")
        total += expense['amount']
    print(f"\nTotal: ${total:.2f}")

def main():
    initialize_expenses()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
