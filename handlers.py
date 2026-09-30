def handle_add_task(todo_list):
    description = input("Enter task description: ")
    todo_list.add_task(description)


def handle_update_task(todo_list):
    try:
        task_id = int(
            input("Enter the ID of the task to update: ")
        )

        print("What do you want to update?")
        print("  a. Description")
        print("  b. Status (Completed/Pending)")
        print("  c. Both")

        update_choice = input(
            "Enter your choice (a/b/c): "
        ).lower()

        new_description = None
        new_status = None

        if update_choice in ("a", "c"):
            new_description = input("Enter new description: ")

        if update_choice in ("b", "c"):
            status_input = input(
                "Mark as completed? (yes/no): "
            ).lower()

            new_status = status_input == "yes"

        if new_description is not None or new_status is not None:
            todo_list.update_task(
                task_id,
                new_description,
                new_status
            )
        else:
            print("No update specified or invalid choice.")

    except ValueError:
        print("Invalid task ID. Please enter a number.")


def handle_delete_task(todo_list):
    try:
        task_id = int(
            input("Enter the ID of the task to delete: ")
        )

        todo_list.delete_task(task_id)

    except ValueError:
        print("Invalid task ID. Please enter a number.")
