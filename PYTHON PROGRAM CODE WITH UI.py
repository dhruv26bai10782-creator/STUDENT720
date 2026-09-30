                                  # TodoList Crud Application (VITYARTHI PROJECT)

                                  
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import font as tkfont 

class TodoList:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1

    def add_task(self, description):
        task = {"id": self.task_id_counter, "description": description, "completed": False}
        self.tasks.append(task)
        self.task_id_counter += 1
        return task['id']

    def get_tasks(self):
        return [
            f"ID: {t['id']} | {' ✅ ' if t['completed'] else ' '}: {t['description']}" 
            for t in self.tasks
        ]

    def find_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def update_task(self, task_id, new_description=None, new_status=None):
        task = self.find_task(task_id)
        if task:
            if new_description is not None:
                task["description"] = new_description
            if new_status is not None:
                task["completed"] = new_status
            return True
        return False

    def delete_task(self, task_id):
        initial_len = len(self.tasks)
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        return len(self.tasks) < initial_len


class TodoApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")
        self.todo_list = TodoList()
        

        self.BG_COLOR = "#F5F5DC"        
        self.ACCENT_BG = "#FFF8DC"      
        self.TEXT_COLOR = "#556B2F"      
        self.LISTBOX_BG = "#FFFAF0"      
        

        self.ADD_COLOR = "#F0F8FF"       
        self.TOGGLE_COLOR = "#008080"   
        self.EDIT_COLOR = "#FFA07A"      
        self.DELETE_COLOR = "#CD5C5C"    
        self.BUTTON_FG = "#B22222"       
        
        self.FONT_FAMILY = 'Arial'
        

        master.config(bg=self.BG_COLOR)
        

        self.title_font = tkfont.Font(family=self.FONT_FAMILY, size=18, weight='bold')
        self.regular_font = tkfont.Font(family=self.FONT_FAMILY, size=10)


        self.title_label = tk.Label(
            master, 
            text="To Do List Task Manager", 
            font=self.title_font, 
            bg=self.BG_COLOR, 
            fg=self.TEXT_COLOR 
        )
        self.title_label.pack(pady=(20, 10))


        self.input_frame = tk.Frame(master, bg=self.ACCENT_BG)
        self.input_frame.pack(pady=10, padx=20, fill='x')

        self.task_entry = tk.Entry(
            self.input_frame, 
            width=50, 
            font=self.regular_font, 
            relief=tk.FLAT, 
            bd=2, 
            highlightthickness=1,
            highlightbackground=self.TEXT_COLOR,
            highlightcolor=self.ADD_COLOR
        )
        self.task_entry.pack(side=tk.LEFT, fill='x', expand=True, padx=(10, 10), ipady=4)
        self.task_entry.bind('<Return>', lambda event: self.add_task())

        self.add_button = tk.Button(
            self.input_frame, 
            text="➕ Add Task", 
            command=self.add_task,
            bg=self.ADD_COLOR, 
            fg=self.BUTTON_FG, 
            relief=tk.FLAT, 
            font=self.regular_font,
            activebackground="#ADFF2F" 
        )
        self.add_button.pack(side=tk.RIGHT, ipadx=10, ipady=4, padx=(0, 10))


        self.listbox_frame = tk.Frame(master, bg=self.BG_COLOR)
        self.listbox_frame.pack(padx=20, pady=5)

        self.task_listbox = tk.Listbox(
            self.listbox_frame, 
            width=60, 
            height=15,
            bg=self.LISTBOX_BG,
            fg=self.TEXT_COLOR,
            font=self.regular_font,
            selectbackground=self.ACCENT_BG, 
            selectforeground=self.TEXT_COLOR,
            bd=1, 
            relief=tk.RIDGE, 
            highlightthickness=0 
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.listbox_frame, orient="vertical", command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        

        self.task_listbox.bind('<Enter>', self.on_listbox_enter)
        self.task_listbox.bind('<Leave>', self.on_listbox_leave)


        self.button_frame = tk.Frame(master, bg=self.BG_COLOR)
        self.button_frame.pack(pady=(10, 20))


        button_kwargs = {
            'fg': self.BUTTON_FG,
            'relief': tk.FLAT,
            'font': ('Arial', 10, 'bold'), 
            'padx': 10,
            'pady': 5
        }


        self.complete_button = tk.Button(
            self.button_frame, 
            text="🔁 Toggle Status", 
            command=self.toggle_task_status,
            bg=self.TOGGLE_COLOR, 
            activebackground="#B22222",
            **button_kwargs
        )
        self.complete_button.pack(side=tk.LEFT, padx=5)


        self.update_button = tk.Button(
            self.button_frame, 
            text="✏️ Edit Description", 
            command=self.edit_task_description,
            bg=self.EDIT_COLOR, 
            activebackground="#B22222",
            **button_kwargs
        )
        self.update_button.pack(side=tk.LEFT, padx=5)


        self.delete_button = tk.Button(
            self.button_frame, 
            text="🗑️ Delete Task", 
            command=self.delete_task,
            bg=self.DELETE_COLOR, 
            activebackground="#B22222",
            **button_kwargs
        )
        self.delete_button.pack(side=tk.LEFT, padx=5)


        self.refresh_listbox()


    def on_listbox_enter(self, event):
        """Changes listbox border color on mouse hover."""
        self.task_listbox.config(highlightthickness=1, highlightbackground=self.TEXT_COLOR)
    def on_listbox_leave(self, event):
        """Removes listbox border color when mouse leaves."""
        self.task_listbox.config(highlightthickness=0)

        
    def get_selected_task_id(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            selected_text = self.task_listbox.get(selected_index)
            task_id_str = selected_text.split('|')[0].split(':')[1].strip()
            return int(task_id_str)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task from the list.")
            return None

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task_string in self.todo_list.get_tasks():
            self.task_listbox.insert(tk.END, task_string)

    def add_task(self):
        description = self.task_entry.get().strip()
        if description:
            self.todo_list.add_task(description)
            self.task_entry.delete(0, tk.END)
            self.refresh_listbox()
        else:
            messagebox.showwarning("Warning", "Task description cannot be empty.")

    def delete_task(self):
        task_id = self.get_selected_task_id()
        if task_id is not None:
            if self.todo_list.delete_task(task_id):
                self.refresh_listbox()
            else:
                messagebox.showerror("Error", "Task not found.")

    def toggle_task_status(self):
        task_id = self.get_selected_task_id()
        if task_id is not None:
            task = self.todo_list.find_task(task_id)
            if task:
                new_status = not task['completed']
                self.todo_list.update_task(task_id, new_status=new_status)
                self.refresh_listbox()

    def edit_task_description(self):
        task_id = self.get_selected_task_id()
        if task_id is not None:
            task = self.todo_list.find_task(task_id)
            if task:
                new_description = simpledialog.askstring(
                    "Edit Task", 
                    "Enter the new task description:", 
                    initialvalue=task['description']
                )
                
                if new_description is None:
                    return
                
                if not new_description.strip():
                    messagebox.showwarning("Warning", "Description cannot be empty.")
                    return
                
                if new_description.strip() != task['description']:
                    self.todo_list.update_task(task_id, new_description=new_description.strip())
                    self.refresh_listbox()


if __name__ == "__main__":
    root = tk.Tk()
    try:
        root.tk.call("source", "azure.tcl")
    except tk.TclError:
        pass 
        
    app = TodoApp(root)
    root.mainloop()
