import csv

# Inventory dictionary to store products (product_name: [quantity, price])
inventory = {}

def add_product():
    name = input("Enter product name: ").strip().lower()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    
    if name in inventory:
        inventory[name][0] += quantity  # Update quantity if product exists
    else:
        inventory[name] = [quantity, price]
    
    print(f"Product '{name}' added successfully!\n")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("Current Inventory:")
    print("Name\tQuantity\tPrice")
    for name, details in inventory.items():
        print(f"{name}\t{details[0]}\t${details[1]:.2f}")
    print()

def update_stock():
    print("update_stock")

def delete_product():
    print("delete_product")

# Complete the below function ---------------
def search_product():
    if not inventory:
        print("Inventory is empty.")
        return
    searched_product=input("Enter Product Name: ")
    if searched_product in inventory:
        print(f"{searched_product}:")
        print(f"Quantity={inventory[searched_product][0]},Price=${inventory[searched_product][0]:.2f}")
    else:
        print("Product not Found")
def save_inventory():
    print("save_inventory")
if __name__ == "__main__":
    
    while True:
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
