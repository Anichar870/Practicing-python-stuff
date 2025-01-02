# Simple ATM Simulator

# Initial balance
balance = 1000

def display_menu():
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

# ATM functionality
while True:
    display_menu()
    
    # Get user choice
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        # Check balance
        print(f"\nYour current balance is: ₹{balance}")
    elif choice == 2:
        # Deposit money
        amount = float(input("\nEnter the amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            print(f"₹{amount} has been deposited successfully!")
        else:
            print("Invalid amount. Please enter a positive value.")
    elif choice == 3:
        # Withdraw money
        amount = float(input("\nEnter the amount to withdraw: ₹"))
        if 0 < amount <= balance:
            balance -= amount
            print(f"₹{amount} has been withdrawn successfully!")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            print("Invalid amount. Please enter a positive value.")
    elif choice == 4:
        # Exit the program
        print("\nThank you for using the ATM. Have a great day!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
