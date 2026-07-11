# Dictionary to store contacts
contacts = {}


# Update the code below to solve the problem
#-------------------------------------------------
def add_contact():
    name=input("Enter Name:")
    ph=input("Enter a Number:").strip()
    if not ph.isdigit() or name==None or len(ph)!=10:
        print("Invalid! Please enter a valid name and 10-digit phone number")
    elif ph in contacts:
        print("Contact Already exists!")
    else:
        contacts[ph]=name
        print(f"Conatct '{name}' added sucessfully!")


    """Adds a new contact."""
    



#-------------------------------------------------  
    
def view_contacts():
    """Displays all contacts."""
    
def search_contact():
    """Searches for a contact."""
    
def update_contact():
    """Updates a contact."""

def delete_contact():
    """Deletes a contact."""
    
# Update the function to handle user input
def userChoice(choice):
    """Handles user input and calls the corresponding function."""
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")

# Main execution loop
if __name__ == '__main__':
    while True:
        print("\n📞 Contact Manager Menu:")
        print("1. Add a Contact")
        print("2. View Contacts")
        print("3. Search for a Contact")
        print("4. Update a Contact")
        print("5. Delete a Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        userChoice(choice)
