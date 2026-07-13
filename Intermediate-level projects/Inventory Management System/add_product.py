import csv

# Inventory dictionary to store products (product_name: [quantity, price])
inventory = {}

# Task: Implement this function-------------------
def add_product():
    pname=input("Enter product name")
    quan=input("Enter Quantity")
    ppu=input("Enter Price per Unit ")
    if pname in inventory:
        inventory[pname][0]+=quan
    else:
        inventory[pname]=[quan,ppu]
    print(f"Product '{pname}' added sucessfully")


    """Adds a new product to the inventory with proper validation."""








# -------------------------------------------------


def view_inventory():
    # For Viewing Inventory
    print("View")

def update_stock():
    # For Updating Stock
    print("Update")

def delete_product():
    # For Deleting Inventory
    print("Delete")

def search_product():
    # For Searching a Product
    print("Search")

def save_inventory():
    # Saving in inventory
    print("Save")

if __name__ == "__main__":

    while(True):
        print("1. Add Product\n2. View Inventory\n3. Update Stock\n4. Delete Product\n5. Search Product\n6. Save & Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            search_product()
        elif choice == "6":
            save_inventory()
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.\n")
