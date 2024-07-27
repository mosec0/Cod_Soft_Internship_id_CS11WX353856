import json

# File to save tasks
TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f)

# Display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{idx}. {task['title']} - {status}")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Task added.")

# Update an existing task
def update_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number to update: "))
    if 0 < task_num <= len(tasks):
        new_title = input("Enter new task title: ")
        tasks[task_num - 1]["title"] = new_title
        save_tasks(tasks)
        print("Task updated.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number to delete: "))
    if 0 < task_num <= len(tasks):
        tasks.pop(task_num - 1)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid task number.")

# Mark a task as completed
def complete_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: "))
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

# Main function to run the command-line interface
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List:")
        display_tasks(tasks)
        print("\nOptions:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            update_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            print("Exiting To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
