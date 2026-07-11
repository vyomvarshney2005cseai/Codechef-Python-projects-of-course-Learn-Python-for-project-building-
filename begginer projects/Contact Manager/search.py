
# Dictionary to store contacts
contacts = {}

def add_contact():
    """Adds a new contact to the dictionary."""
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number (10 digits): ").strip()

    if not name or not phone.isdigit() or len(phone) != 10:
        print("Invalid input! Please enter a valid name and 10-digit phone number.")
        return

    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[phone] = name
        print(f"Contact '{name}' added successfully!")

def view_contacts():
    """Displays all saved contacts."""
    if not contacts:
        print("No contacts available!")
        return

    print("\nContact List:")
    for phone, name in contacts.items():
        print(f"{name}: {phone}")
        return


# Update the code below to solve the problem
#-------------------------------------------------
def search_contact():
    namefromuser=input("Enter name/phone number to search: ")
    for phone,name in contacts.items():
        if name==namefromuser or phone==namefromuser:
            print(f"{name}: {phone}")
            return
        print("Contact not found!")


    


#-------------------------------------------------      

def update_contact():
    """Updates an existing contact (name or phone number)."""

def delete_contact():
    """Deletes a contact by name."""

def userChoice(choice):
    """Handles user input and calls the appropriate function."""
    
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
