<h2>Explanation</h2>

    Data Structure:
        We use a list of dictionaries to store tasks, where each task is represented as a dictionary with title and completed fields.

    Loading and Saving Tasks:
        Tasks are saved to and loaded from a JSON file (tasks.json). This allows persistent storage of tasks between runs.

    Functions:
        load_tasks(): Loads tasks from the JSON file.
        save_tasks(tasks): Saves the current list of tasks to the JSON file.
        display_tasks(tasks): Displays the current tasks with their status (Done/Not Done).
        add_task(tasks): Adds a new task to the list.
        update_task(tasks): Updates the title of an existing task.
        delete_task(tasks): Deletes a task from the list.
        complete_task(tasks): Marks a task as completed.

    Main Function:
        The main() function provides a simple command-line interface for the user to interact with the To-Do List application. It repeatedly displays the list of tasks and prompts the user to choose an action until they choose to exit.

<h2>Running the Application</h2>

To run the application, save the code to a file (e.g., todo_list.py) and execute it with Python:

python3 todo_list.py

<h2>This will start the command-line interface, allowing you to add, update, delete, and mark tasks as completed. The tasks are saved to tasks.json, so they persist between runs of the application</h2>
