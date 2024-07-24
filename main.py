import json
import os

TODO_FILE = "todos.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=4)

def display_todos(todos):
    if not todos:
        print("No tasks to display.")
    for i, todo in enumerate(todos, start=1):
        print(f"{i}. {todo}")

def main():
    todos = load_todos()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            todos.append(task)
            save_todos(todos)
            print("Task added.")
        elif choice == "2":
            display_todos(todos)
            try:
                index = int(input("Enter task number to remove: ")) - 1
                if 0 <= index < len(todos):
                    removed = todos.pop(index)
                    save_todos(todos)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            display_todos(todos)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

