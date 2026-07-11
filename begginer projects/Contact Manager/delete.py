
# Contact Manager - Simple Dictionary-Based Implementation

# Dictionary to store contacts
contacts = {}

def add_contact():
    """Adds a new contact to the dictionary."""
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number (10 digits): ").strip()

    if not name or not phone.isdigit() or len(phone) != 10:
        print("Invalid input! Please enter a valid name and 10-digit phone number.")
        return

    if phone in contacts:
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

def search_contact():
    """Search contacts by name or phone number.
    Args:
        contacts: Dictionary of {phone: name} pairs
    """
    query = input("Enter name or phone number to search: ").strip()

    # First try direct phone number lookup
    if query in contacts:
        print(f"{contacts[query]}: {query}")
        return

    # Then search by name (case-insensitive)
    found = False
    for phone, name in contacts.items():
        if name.lower() == query.lower():
            print(f"{name}: {phone}")
            found = True

    if not found:
        print("Contact not found!")

def update_contact():
    """Updates an existing contact (name or phone number)."""
    if not contacts:
        print("No contacts available to update!")
        return
    
    # Get phone number of contact to update
    phone = input("Enter phone number to update name: ").strip()
    
    # Check if contact exists
    if phone not in contacts:
        print(f"Contact with phone '{phone}' not found!")
        return
    
    current_name = contacts[phone]
    
    # Get new name
    new_name = input(f"Current name: {current_name}\nEnter new name: ").strip()
    
    # Validate new name
    if not new_name:
        print("Name cannot be empty!")
        return

    
    # Update the name
    contacts[phone] = new_name
    print(f"Successfully updated name to: {new_name} ({phone})")


# Update the code below to solve the problem
#-------------------------------------------------
def delete_contact():
    """Deletes a contact by name."""
    if not contacts:
        print("No contacts Available: ")
    ntd=input("Enter name to delete:").strip()
    ptd=None
    for name,phone in contacts.items():
        if name.lower()==ntd.lower():
            ptd=phone
            break
    if not ptd:
        print(f"No contacts found with name '{ntd}'")
        return
    del contacts[ptd]
    print(f"Contact '{ntd}' deleted sucessfully!")












#-------------------------------------------------

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
