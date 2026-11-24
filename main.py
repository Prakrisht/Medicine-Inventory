from inventory import read_medicine_data, display_inventory
from sell import sell_medicine
from restock import restock_medicine

file_path = "medicine_inventory.txt"

def main():
    """
    Main function that runs the MedStore Wholesale System.
    Reads the inventory file on startup, displays the medicine table,
    and runs the main menu in a loop until the user chooses to exit.

    Args:
        None

    Returns:
        None
    """
    # read inventory data from file 
    inventory = read_medicine_data(file_path)
    if len(inventory) == 0:
        print("Error: Inventory is empty.")
        return
    
    print("\n Welcome to MedStore Wholesale System")
    display_inventory(inventory)
    
    while True:
        print("\n"+ "=" * 30)
        print("Main Menu")
        print("=" * 30)
        print("1. Sell Medicine")
        print("2. Restock Medicine")
        print("3. View Inventory")
        print("4. Exit")
        print("=" * 30)
        
        choice = input("Enter your choice(1-4): ").strip()

        if choice == "1":
            sell_medicine(inventory)
        elif choice == "2":
            restock_medicine(inventory)
        elif choice == "3":
            print("\n")
            display_inventory(inventory)
        elif choice == "4":
            print("Thank you for using MedStore System!")
            break
        
        else:
            print("Error: Invalid choice. Please enter between 1 to 4.")
        
main()
