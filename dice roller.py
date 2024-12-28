import random

def dice_roller():
    print("Welcome to the Dice Roller!")
    
    while True:
        roll = input("\nPress 'r' to roll the dice or 'q' to quit: ").lower()
        if roll == 'r':
            dice = random.randint(1, 6)
            print(f"You rolled a {dice}!")
        elif roll == 'q':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please press 'r' to roll or 'q' to quit.")

if __name__ == "__main__":
    dice_roller()
