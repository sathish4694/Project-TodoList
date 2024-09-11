import json
import os

# Define the file path where tasks will be saved
Todo_List = r'D:\Miraclesoft\To-DoListApplication\Housetasks.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(Todo_List):
        with open(Todo_List, 'r') as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks():
    with open(Todo_List, 'w') as file:
        json.dump(tasks, file, indent=4)

# Initialize tasks from file
tasks = load_tasks()

def add_task():
    category_name = input("Enter category name: ")
    task_name = input("Enter task name: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    status = input("Enter status: ")
    remarks = input("Enter remarks: ")
    tasks.append({"category_name": category_name, "task_name": task_name, "due_date": due_date, "status": status, "remarks": remarks })
    save_tasks()
    print("Task added successfully.")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks):
            print(f"{idx + 1}. {task['task_name']} (Category: {task['category_name']}, Due: {task['due_date']}, Status: {task['status']}, Remarks: {task['remarks']})")


def edit_task():
    view_tasks()
    task_index = int(input("Enter the task number to edit: ")) - 1
    if 0 <= task_index < len(tasks):
        new_category_name = input("Enter new category name: ")
        new_task_name = input("Enter new task name: ")
        new_due_date = input("Enter new due date: ")
        new_status = input("Enter new status : ")
        new_remarks = input("Enter new remarks: ")
        tasks[task_index] = {"category_name": new_category_name, "task_name": new_task_name, "due_date": new_due_date, "status": new_status, "remarks": new_remarks}
        save_tasks()
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks()
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

while True:
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Edit a task")
    print("4. Delete a task")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        edit_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
