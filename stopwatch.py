import time

def display_menu():
    print("\nStopwatch Menu:")
    print("1. Start Stopwatch")
    print("2. Stop Stopwatch")
    print("3. Reset Stopwatch")
    print("4. Exit")

def stopwatch():
    running = False
    start_time = None
    elapsed_time = 0

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":  # Start
            if not running:
                start_time = time.time() - elapsed_time
                running = True
                print("Stopwatch started.")
            else:
                print("Stopwatch is already running.")
        
        elif choice == "2":  # Stop
            if running:
                elapsed_time = time.time() - start_time
                running = False
                print(f"Stopwatch stopped. Elapsed time: {elapsed_time:.2f} seconds.")
            else:
                print("Stopwatch is not running.")

        elif choice == "3":  # Reset
            elapsed_time = 0
            start_time = None
            running = False
            print("Stopwatch reset.")

        elif choice == "4":  # Exit
            print("Exiting stopwatch. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select from the menu.")

        if running:
            elapsed_time = time.time() - start_time
            print(f"Elapsed time: {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    stopwatch()
