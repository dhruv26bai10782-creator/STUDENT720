# Project Title:  To-Do List CRUD Application


# Overview of the Project

Hello! This is a simple To-Do List application designed as a Python desktop utility. The project is contained in a single Python file and aims to provide a clean graphical user interface for managing your daily tasks.  

I used the Object-Oriented Programming (OOP) method to develop this application. The main logic for handling tasks—adding, deleting, and updating—was completely separated from the user interface, which includes buttons and lists. This separation makes it easier to understand and expand the code later. Think of it like having a "Task Manager" object as a background service that interacts with the "Window" object only when it needs to show or change something.  

Currently, tasks are stored in temporary memory and will be lost once the application is closed. However, it is easy to add features for permanent storage in the future!  



# Features

This application simulates the entire process users need to manage their tasks:  

1. Task Creation: There is an input field and an "➕ Add Task" button, or you can press {Enter} to quickly add a new task.  

2. Intuitive Display: All tasks are shown in a vertical list that can be scrolled through. Each task has a unique {ID} tag for easy reference and management.  

3. Status Tracking: With the {"🔁 Toggle Status"} button, you can easily mark a task as done or undone. Completed tasks display a {'✅'} icon next to them.  

4. Editing: The {"✏️ Edit Description"} button opens a small dialog box that lets you quickly fix mistakes or update tasks without re-entering everything.  

5. Deletion: Use the {"🗑️ Delete Task"} button to permanently delete a task.  

6. Error Handling: There are safety checks in place, so you cannot add an empty task.






# Technologies/Tools Used


The project brings along a basic, common Python configuration which makes the installation of dependencies not being a problem at all, since there are none!


1- Primary Language: (Python 3.x)

2- GUI Framework: (Tkinter) (Python's standard library for building desktop applications).

3- Libraries: The remaining features depend on Python's standard library modules (`tkinter.messagebox`, `tkinter.simpledialog`, etc.).



# Steps to Install & Run the Project

Since this project only uses Python's standard library, installation is quick and easy!  

Prerequisites  
Make sure Python 3.x is installed on your machine (version 3.6 or higher is recommended).  

Get the Code  
Clone this repository or download the file containing the source code (to do list.py, assuming you saved the code in a single file).  

Launch the Program  
Open the command prompt (TERMINAL).  

Change to the directory where the Python file is stored.  

Run the script using the Python interpreter (IDLE):  

python to do list.py  
The To-Do List window will appear right after execution.  



# Instructions for Testing

To ensure everything works correctly, manually perform the following test scenarios.  

| Test Case          | Steps to Execute                                                        | Expected Outcome                               |  
|--------------------|------------------------------------------------------------------------|------------------------------------------------|  
| 1. Add a Task      | Enter "Finish README" in the input box and hit {Enter} (or click 'Add Task'). | The task appears in the list with an ID assigned and no '✅'. |  
| 2. Toggle Status    | Click on the task you just created. Press the {"🔁 Toggle Status"} button. | The task now shows a '✅' icon, confirming it is completed. |  
| 3. Edit a Task      | Select a task and click {"✏️ Edit Description"}. Enter new text and click OK. | The list updates instantly with the new description. |  
| 4. Delete a Task    | Select any task. Click {"🗑️ Delete Task"}.                             | The selected task disappears from the list.   |  
| 5. Input Validation  | Click the {"➕ Add Task"} button while the input box is empty.          | A message box pops up, and no new task is added. |  
| 6. No Selection Error| Ensure no task is highlighted. Click the {"🗑️ Delete Task"} button.     | A message box pops up, asking you to select a task first. |




# Screenshots

@MAIN INTERFACE

<img width="1470" height="403" alt="MAIN INTERFACE" src="https://github.com/user-attachments/assets/a08755c4-264f-4743-9401-de7e02be1b24" />

@INTERFACE AFTER ADDING TASK

<img width="527" height="429" alt="INTERFACE AFTER ADDING TASK" src="https://github.com/user-attachments/assets/55e0e2a7-1c0a-4447-9ce8-a7b6b34a820e" />

@INTERFACE AFTER CHANGING STATUS OF TASK

<img width="518" height="406" alt="INTERFACE AFTER CHANGING STATUS OF TASK" src="https://github.com/user-attachments/assets/60980b68-7872-4796-a5af-08559c271938" />

@INTERFACE WHILE EDITING DESCRIPTION

<img width="750" height="519" alt="INTERFACE WHILE EDITING DESCRIPTION" src="https://github.com/user-attachments/assets/2dc247b3-0ebe-4362-9520-f0f0d3c44d25" />

@INTERFACE WHILE DELETING TASK

<img width="521" height="407" alt="INTERFACE WHILE DELETING TASK" src="https://github.com/user-attachments/assets/e99b4589-726e-450f-a1e9-54df7723d080" />

@INTERFACE WHILE ADDING TASK

<img width="573" height="446" alt="INTERFACE WHILE ADDING TASK" src="https://github.com/user-attachments/assets/8e2e0b0b-5cca-40b0-8ac8-a8f03d88abf1" />
