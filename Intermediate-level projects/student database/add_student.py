FILE_NAME = "/Users/vyomvarshney2005/Desktop/codechef python projects/Intermediate-level projects/student database/students.txt"

# Update the code below to solve the problem
#-------------------------------------------------
def add_student():
    rno=(input("Enter Roll number: "))
    if not rno.isdigit():
        print("Invalid Roll Number!")
        return
    with open(FILE_NAME,'r') as file:
        for line in file:
            if line.startswith(rno+","):
                print("Student Roll no. existed")
                return
    fname=input("Enter First Name: ")
    if not fname.isalpha():
        print("Invalid Roll Number! It should contain only numbers.")
        return
    age=int(input("Enter Age: "))
    if age>100:
        print("Age must smaller than 100")
        return 
    course=input("Enter Course: ")
    department=input("Enter Department: ")
    with open(FILE_NAME,'a') as file:
        file.write(f"{rno},{fname},{age},{course},{department}\n")
    print("Student Added Successfully!")

    """Function to add a new student record to the file."""
#------------------------------------------------- 

def view_students():
    """Function to display all student records from the file."""
    
def search_student(return_data=False):
    """Function to search for a student by ID or Name."""
   

def update_student():
    """Function to update an existing student record in the file."""
    

def delete_student():
    """Function to delete a student record from the file."""

def user_choice(choice):
    """Handles user input and calls the corresponding function."""
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting Student Database Manager...")
        return
    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == '__main__':
    while True:
        print("\n Student Database Manager")
        print("1. Add a Student")
        print("2. View All Students")
        print("3. Search Student by ID or Name")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()
        user_choice(choice)
        if(choice==6):
            break
