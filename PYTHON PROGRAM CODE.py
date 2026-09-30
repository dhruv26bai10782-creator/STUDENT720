                     # TodoList Crud Application WITHOUT UI (VITYARTHI PROJECT)


class TodoList:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1

    def add_task(self, description):
        task = {"id": self.task_id_counter, "description": description, "completed": False}
        self.tasks.append(task)
        self.task_id_counter += 1
        print(f"Task '{description}' added with ID: {task['id']}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return
        print("\n--- Your To-Do List ---")
        for task in self.tasks:
            status = "(Completed)" if task["completed"] else "(Pending)"
            print(f"ID: {task['id']}, Description: {task['description']} {status}")
        print("-----------------------\n")

    def update_task(self, task_id, new_description=None, new_status=None):
        for task in self.tasks:
            if task["id"] == task_id:
                if new_description is not None:
                    task["description"] = new_description
                    print(f"Task {task_id} description updated to '{new_description}'.")
                if new_status is not None:
                    task["completed"] = new_status
                    status_text = "completed" if new_status else "pending"
                    print(f"Task {task_id} marked as {status_text}.")
                return True
        print(f"Task with ID {task_id} not found.")
        return False

    def delete_task(self, task_id):
        initial_len = len(self.tasks)
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        if len(self.tasks) < initial_len:
            print(f"Task with ID {task_id} deleted.")
            return True
        print(f"Task with ID {task_id} not found.")
        return False

def main():
    todo_list = TodoList()

    def handle_add_task():
        description = input("Enter task description: ")
        todo_list.add_task(description)

    def handle_update_task():
        try:
            task_id = int(input("Enter the ID of the task to update: "))
            print("What do you want to update?")
            print("  a. Description")
            print("  b. Status (Completed/Pending)")
            print("  c. Both")
            update_choice = input("Enter your choice (a/b/c): ").lower()

            new_description = None
            new_status = None

            if update_choice in ('a', 'c'):
                new_description = input("Enter new description: ")
            if update_choice in ('b', 'c'):
                status_input = input("Mark as completed? (yes/no): ").lower()
                new_status = True if status_input == 'yes' else False

            if new_description is not None or new_status is not None:
                todo_list.update_task(task_id, new_description, new_status)
            else:
                print("No update specified or invalid choice.")
        except ValueError:
            print("Invalid task ID. Please enter a number.")

    def handle_delete_task():
        try:
            task_id = int(input("Enter the ID of the task to delete: "))
            todo_list.delete_task(task_id)
        except ValueError:
            print("Invalid task ID. Please enter a number.")

    menu_options = {
        '1': ("Add Task", handle_add_task),
        '2': ("View Tasks", todo_list.view_tasks),
        '3': ("Update Task", handle_update_task),
        '4': ("Delete Task", handle_delete_task),
        '5': ("Exit", None) # None indicates exit
    }

    while True:
        print("\n===== To-Do List Application =====")
        for key, (description, _) in menu_options.items():
            print(f"{key}. {description}")

        choice = input("Enter your choice: ").lower()

        if choice == '5':
            print("Exiting To-Do List Application. Goodbye!")
            break

        action = menu_options.get(choice)
        if action and action[1]: # Check if action exists and is not None (for Exit)
            action[1]()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
