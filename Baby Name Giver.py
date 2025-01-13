import random

# Welcome message
def welcome():
    print("Welcome to the Baby Name Generator!")
    print("Here, you can find the perfect name for your baby based on your preferences.")
    print("\n")

# Define name categories
boys_names = ["Aarav", "Vivaan", "Reyansh", "Advik", "Sai", "Arjun", "Rudra", "Ishaan", "Vihaan", "Kian"]
girls_names = ["Aadhya", "Anaya", "Pari", "Myra", "Ira", "Kiara", "Avni", "Saanvi", "Diya", "Riya"]
neutral_names = ["Arya", "Sam", "Krishna", "Akira", "Daksha", "Rishi", "Harsha", "Shiv", "Shan", "Dev"]

# Function to get user preference
def get_preference():
    print("What type of name are you looking for?")
    print("1. Boy")
    print("2. Girl")
    print("3. Gender Neutral")
    print("\n")
    choice = input("Enter your choice (1/2/3): ")
    return choice

# Function to generate a random name
def generate_name(choice):
    if choice == "1":
        name = random.choice(boys_names)
    elif choice == "2":
        name = random.choice(girls_names)
    elif choice == "3":
        name = random.choice(neutral_names)
    else:
        name = None
    return name

# Function to display the generated name
def display_name(name):
    if name:
        print(f"\nHere is a beautiful name for your baby: {name}")
    else:
        print("\nInvalid choice. Please try again.")

# Main function
def main():
    welcome()
    while True:
        choice = get_preference()
        name = generate_name(choice)
        display_name(name)
        retry = input("\nWould you like to try again? (yes/no): ").strip().lower()
        if retry != "yes":
            print("\nThank you for using the Baby Name Generator. Best wishes!")
            break

if __name__ == "__main__":
    main()
