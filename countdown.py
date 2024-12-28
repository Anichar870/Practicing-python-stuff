import time

def countdown_timer():
    print("Welcome to the Countdown Timer!")
    
    try:
        seconds = int(input("Enter the time in seconds: "))
        print("Countdown started!")
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(timer, end="\r")  # Updates the timer on the same line
            time.sleep(1)
            seconds -= 1
        
        print("\nTime's up!")
    except ValueError:
        print("Please enter a valid number of seconds.")

if __name__ == "__main__":
    countdown_timer()
