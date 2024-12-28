# Simple To-Do List App

# Initialize an empty task list
tasks = []

def display_menu():
    print("\n=== To-Do List Menu ===")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks in the list!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def remove_task():
    if not tasks:
        print("\nNo tasks to remove!")
        return
    
    view_tasks()
    try:
        task_number = int(input("\nEnter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice! Please select from the menu.")

if __name__ == "__main__":
    main()
