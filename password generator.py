import random
import string

def generate_password(length=12, use_special=True, use_numbers=True):
    """
    Generate a random password.

    :param length: Length of the password.
    :param use_special: Include special characters if True.
    :param use_numbers: Include numbers if True.
    :return: Randomly generated password.
    """
    # Define character pools
    letters = string.ascii_letters
    digits = string.digits if use_numbers else ""
    special_chars = string.punctuation if use_special else ""

    # Combine pools
    all_chars = letters + digits + special_chars

    if not all_chars:
        raise ValueError("No character set selected for password generation.")

    # Generate password
    password = "".join(random.choices(all_chars, k=length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        use_special = input("Include special characters? (y/n, default y): ").lower() != 'n'
        use_numbers = input("Include numbers? (y/n, default y): ").lower() != 'n'

        password = generate_password(length, use_special, use_numbers)
        print("\nYour generated password is:")
        print(password)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
