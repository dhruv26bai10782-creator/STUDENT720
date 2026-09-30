from todo_list import TodoList
from menu import run_menu


def main():
    todo_list = TodoList()
    run_menu(todo_list)


if __name__ == "__main__":
    main()
