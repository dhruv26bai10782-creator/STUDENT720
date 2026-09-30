from handlers import (
    handle_add_task,
    handle_update_task,
    handle_delete_task
)


def run_menu(todo_list):

    menu_options = {
        "1": ("Add Task", lambda: handle_add_task(todo_list)),
        "2": ("View Tasks", todo_list.view_tasks),
        "3": ("Update Task", lambda: handle_update_task(todo_list)),
        "4": ("Delete Task", lambda: handle_delete_task(todo_list)),
        "5": ("Exit", None)
    }

    while True:
        print("\n===== To-Do List Application =====")

        for key, (description, _) in menu_options.items():
            print(f"{key}. {description}")

        choice = input("Enter your choice: ").lower()

        if choice == "5":
            print("Exiting To-Do List Application. Goodbye!")
            break

        action = menu_options.get(choice)

        if action and action[1]:
            action[1]()
        else:
            print("Invalid choice. Please try again.")
