from datetime import datetime

# --- YOU NEED TO IMPLEMENT THIS FUNCTION ---
def userChoice(choice, tasks):
    # TODO: Implement the logic based on the 'choice' parameter
    # 1. Add Task: get task_name, deadline, call add_task()
    # 2. Delete Task: get task_number, call delete_task()
    # 3. Display Tasks: call display_tasks()
    # 4. Exit: return "Exiting application. Goodbye!"
    # Else: print "Invalid choice!"
    pass
# --- END OF FUNCTION TO IMPLEMENT ---


def add_task(tasks, task_name, deadline):
    print(f"Task {task_name} - {deadline} added successfully")


def delete_task(tasks, task_number):
    print(f"Task with Task number {task_number} deleted successfully")


def display_tasks(tasks):
    print("Let's display the tasks")


if __name__ == "__main__":
    # # List to store tasks
    tasks = []
    print("""
Welcome to the To-Do List Application!
    """)
    
    while True:
        print("Choose one operation:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        value  = userChoice(choice, tasks)
        if value == "Exiting application. Goodbye!":
            print(value)
            break