from inventory import display_inventory, update_inventory
from invoice import generate_restock_note

file_path = "medicine_inventory.txt"

def get_medicine(inventory, sn):
    """
    Returns the medicine name corresponding to the given serial number.

    Args:
        inventory (dict): The dictionary containing all medicine records.
        sn (int): The serial number of the medicine as displayed in the inventory table.

    Returns:
        str: The medicine name if the serial number is valid, otherwise None.
    """
    medicine_list = list(inventory.keys())
    if sn < 1 or sn > len(medicine_list):
        return None
    return medicine_list[sn - 1]

def restock_medicine(inventory):
    """
    Handles restocking of medicines from a supplier.
    Allows multiple medicines per restock transaction.
    Generates a restock note as a .txt file and updates the inventory file.

    Args:
        inventory (dict): The dictionary containing all medicine records.

    Returns:
        None
    """
    while True:
        supplier_name = input("Enter supplier name : ").strip()
        
        # validate that supplier name is not empty
        if supplier_name == "" :
            print("Error: Supplier name cannnot be empty")
        else:
            break
    
    restocked_items = [] #list to store all restock items 
    grand_total = 0.0
    
    while True:
        print("\n")
        display_inventory(inventory)
        
        sn_input = input("\n Enter medicine S.No. to restock ('0 to stop'): ").strip()
        if sn_input == "0":
            if len(restocked_items) == 0:
                print("Error: No medicine has been selected.")
            break
        
        # validate that input is a valid integer
        try:
            sn = int(sn_input)
        except ValueError:
            print("Error: Please enter a valid medicine serial number.")
            continue
        
        # get medicine name from serial number
        medicine_name = get_medicine(inventory, sn)
        if medicine_name is None:
            print("Error: Invalid medicine S.No. Please try again.")
            continue
    
        if medicine_name not in inventory:
            print(f"Error : {medicine_name} not found in inventory. Please try again")
            continue
        
        print(f"\n Selected medicine : {medicine_name}")
        
        # extract medicine details from inventory
        details = inventory[medicine_name]
        brand = details[0]
        rate_tablet = details[2]
        rate_strip = details[3]
        tablets_per_strip = details[4]
        
        # validate unit type input
        while True:
            unit = input("Enter the unit type (tablet/strip): ").strip().lower()
            if unit == "tablet" or unit == "strip":
                break
            else:
                print("Invalid type of unit. Please enter tablet or strip. ")
        
        
        # validate quantity input
        while True:
            try:
                quantity = int(input("Enter the quantity: ").strip())
                if quantity <= 0:
                    print("Error : Quanity must be greater than zero.")
                    continue
                break
            except ValueError:
                print("Error: Please enter a whole number for quantity. ")
         
         # calculate total and discount based on unit type and quantity       
        if unit == "tablet":
           rate = rate_tablet
           total = quantity * rate_tablet
           inventory[medicine_name][1] += quantity # add quantity to stock in inventory
        elif unit == "strip":
           rate = rate_strip
           total = quantity * rate_strip
           inventory[medicine_name][1] += quantity * tablets_per_strip #convert strip quantity to tablets and add to stock in inventory

        print(f"\n Restock Summary ")
        print(f"Medicine : {medicine_name}")
        print(f"Brand : {brand}")
        print(f"Unit : {unit}")
        print(f"Quantity : {quantity}")
        print(f"Rate : Rs {rate:.2f}")
        print(f"Total : Rs {total:.2f}")
        
        # add item to restocked items
        restocked_items.append({
            "name" : medicine_name,
            "brand" : brand,
            "unit" : unit,
            "quantity" : quantity,
            "rate" : rate,
            "total" : total
        })
        
        grand_total += total
    
    if len(restocked_items) > 0:
        print(f"\n Grand Total: Rs {grand_total:.2f}")
        update_inventory(file_path, inventory)
        generate_restock_note(supplier_name, restocked_items, grand_total)
        print("\n Stock updated successfully.") 