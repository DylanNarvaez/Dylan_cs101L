def add_task(todo_list):
    task_description = input("Enter task description: ")
    todo_list.append({"description": task_description, "completed": False, "priority": None})
    print("Task added successfully.")

def mark_completed(todo_list):
    print("Current To-Do List:")
    display_todo_list(todo_list)
    try:
        index = int(input("Enter the index of the task to mark as completed: "))
        if 0 <= index < len(todo_list):
            todo_list[index]["completed"] = True
            print("Task marked as completed successfully.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def display_todo_list(todo_list):
    if not todo_list:
        print("To-Do List is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list):
            status = "Completed" if task["completed"] else "Pending"
            priority = task["priority"] if task["priority"] else "Not Set"
            print(f"{index}. {task['description']} - Status: {status}, Priority: {priority}")

def prioritize_task(todo_list):
    print("Current To-Do List:")
    display_todo_list(todo_list)
    try:
        index = int(input("Enter the index of the task to prioritize: "))
        if 0 <= index < len(todo_list):
            priority_level = input("Enter priority level (high, medium, low): ").lower()
            if priority_level in ['high', 'medium', 'low']:
                todo_list[index]["priority"] = priority_level
                print("Priority set successfully.")
            else:
                print("Invalid priority level. Please enter either high, medium, or low.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def remove_completed_tasks(todo_list):
    completed_tasks = [task for task in todo_list if task["completed"]]
    if completed_tasks:
        print("Completed Tasks that were removed:")
        for task in completed_tasks:
            print(f"- {task['description']}")
        todo_list[:] = [task for task in todo_list if not task["completed"]]
        print("Completed tasks removed successfully.")
    else:
        print("No completed tasks to remove.")

def main():
    todo_list = []
    while True:
        print("\nMenu Options:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View To-Do List")
        print("4. Prioritize Task")
        print("5. Remove Completed Tasks")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            mark_completed(todo_list)
        elif choice == '3':
            display_todo_list(todo_list)
        elif choice == '4':
            prioritize_task(todo_list)
        elif choice == '5':
            remove_completed_tasks(todo_list)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
