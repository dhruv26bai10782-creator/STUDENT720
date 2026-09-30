from task import Task


class TodoList:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1

    def add_task(self, description):
        task = Task(self.task_id_counter, description)
        self.tasks.append(task)
        self.task_id_counter += 1
        print(f"Task '{description}' added with ID: {task.id}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return

        print("\n--- Your To-Do List ---")

        for task in self.tasks:
            status = "(Completed)" if task.completed else "(Pending)"
            print(
                f"ID: {task.id}, "
                f"Description: {task.description} {status}"
            )

        print("-----------------------\n")

    def update_task(self, task_id, new_description=None, new_status=None):
        for task in self.tasks:
            if task.id == task_id:

                if new_description is not None:
                    task.description = new_description
                    print(
                        f"Task {task_id} description "
                        f"updated to '{new_description}'."
                    )

                if new_status is not None:
                    task.completed = new_status
                    status_text = (
                        "completed" if new_status else "pending"
                    )
                    print(
                        f"Task {task_id} marked as {status_text}."
                    )

                return True

        print(f"Task with ID {task_id} not found.")
        return False

    def delete_task(self, task_id):
        initial_len = len(self.tasks)

        self.tasks = [
            task for task in self.tasks
            if task.id != task_id
        ]

        if len(self.tasks) < initial_len:
            print(f"Task with ID {task_id} deleted.")
            return True

        print(f"Task with ID {task_id} not found.")
        return False
