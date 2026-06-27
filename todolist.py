from datetime import datetime

# --- YOU NEED TO IMPLEMENT THIS FUNCTION ---
def userChoice(choice, tasks):
    # TODO: Implement the logic based on the 'choice' parameter
    # 1. Add Task: get task_name, deadline, call add_task()
    if choice==1:
        task_name=input("Enter task name: ")
        deadline=input("Enter deadline (DD-MM-YY): ")
        add_task(tasks,task_name,deadline)
    # 2. Delete Task: get task_number, call delete_task()
    elif choice==2:
        task_number=int(input("Enter a task number to delete: "))
        delete_task(tasks,task_number)
    elif choice==3:
        display_tasks(tasks)
    elif choice== 4:
        return ("Exiting application. Goodbye!")
    else:
        print("Invalid choice!\n")
    # 3. Display Tasks: call display_tasks()
    # 4. Exit: return "Exiting application. Goodbye!"
    # Else: print "Invalid choice!"

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