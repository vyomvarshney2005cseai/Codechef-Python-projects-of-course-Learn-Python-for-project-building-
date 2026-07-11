from datetime import datetime

def userChoice(choice, tasks):
    if choice == 1:
        task_name = input("Enter task name: ")
        deadline = input("Enter deadline (DD-MM-YYYY): ")
        add_task(tasks, task_name, deadline)
    elif choice == 2:
        task_number = int(input("Enter task number to delete: "))
        delete_task(tasks, task_number)
        print("Let's initiate task deletion")
    elif choice == 3:
        display_tasks(tasks)
    elif choice == 4: 
        return ("Exiting application. Goodbye!")
    else:
        print("Invalid choice!\n")

# Update the Function below to solve the problem
#----------------------------------------------
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    else:
        index=1
        for task in tasks:
            formatted_deadline=task['deadline'].strftime("%d-%m-%Y")
            print(f"{index}.{task['task']} - Deadline: {formatted_deadline}")
            index+=1
    print()

#----------------------------------------------

def validate_date(deadline):
    try:
        deadline_date =  datetime.strptime(deadline, "%d-%m-%Y").date()
        return deadline_date
    except ValueError:
        print("Invalid date format! Try again.\n")


def add_task(tasks, task_name, deadline):
    deadline_date = validate_date(deadline)
    if deadline_date:
        tasks.append({"task": task_name, "deadline": deadline_date})
        print(f"Task '{task_name}' added successfully!\n")


def delete_task(tasks, task_number):
    """Deletes a task from the task list based on user input."""

if __name__ == "__main__":
    # List to store Tasks
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