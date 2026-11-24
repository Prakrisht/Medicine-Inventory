from inventory import display_inventory,update_inventory
from invoice import generate_sales_invoice

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

def sell_medicine(inventory):
    """
    Handles the sale of medicines to a customer.
    Allows multiple medicines per transaction.
    Applies 5% discount when 2 or more strips of the same medicine are purchased.
    Generates a VAT invoice as a .txt file and updates the inventory file.

    Args:
        inventory (dict): The dictionary containing all medicine records.

    Returns:
        None
    """
    while True:
        customer_name = input("Enter customer name : ").strip()
        # validate customer name is not empty
        if customer_name == "" :
            print("Error : Customer name cannnot be empty")
        else:
            break
    
    purchased_items = [] # list to store all items in this transaction
    grand_total = 0.0   
    
    while True:
        print("\n")
        display_inventory(inventory)
        
        sn_input = input("\n Enter medicine S.No. to sell ('0 to stop'): ").strip()
        if sn_input == "0":
            if len(purchased_items) == 0:
                print("Error: No medicine has been selected.")
                return
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
        
        print(f"\n Selected Medicine : {medicine_name}")
        
        # unpack medicine details from inventory
        brand, stock, rate_tablet, rate_strip, tablets_per_strip = inventory[medicine_name]
        
        print(f"\n Available Stock for {medicine_name} : {stock} tablet")
        
        total = 0.0
        discount = 0.0
        
        # validate unit type input
        while True:
            unit = input("\nEnter the unit type (tablet/strip): ").strip().lower()
            if unit == "tablet" or unit == "strip":
                break
            else:
                print("Invalid type of unit. Please enter tablet or strip. ")
        
        # validate quantity input
        while True:
            while True:
                try:
                    quantity = int(input("\nEnter the quantity: ").strip())
                    if quantity <= 0:
                        print("Error : Quanity must be greater than zero.")
                        continue
                    break
                except ValueError:
                    print("Error: Please enter a whole number for quantity. ")
            
            # calculate total and discount based on unit type and quantity
            if unit == "tablet":
                # check if requested quantity is available in stock
                if quantity > stock:
                    print(f"Error: Insufficient stock. Available: {stock} tablets.")
                    continue
                total = quantity * rate_tablet
                discount = 0.0
                break
            
            elif unit == "strip":
                # check if requested quantity in strips is available in stock (convert to tablets)
                required_tablets = quantity * tablets_per_strip
                if required_tablets > stock:
                    available_strips = stock // tablets_per_strip
                    print(f"Error : Insufficient stock. Available: {available_strips} strips.")
                    continue
                
                # apply 5% discount if quantity is 2 or more strips
                if quantity >= 2:
                    discount = (quantity * rate_strip)* 0.05
                    total = (quantity * rate_strip) - discount
                else:
                    discount = 0.0
                    total = quantity * rate_strip
                break
        
        print(f"\n Item Summary ")
        print(f"Medicine : {medicine_name}")
        print(f"Brand : {brand}")
        print(f"Unit : {unit}")
        print(f"Quantity : {quantity}")
        print(f"Discount : Rs {discount:.2f}")
        print(f"Total : Rs {total:.2f}")
        
        # add item to purchased items list
        purchased_items.append({
            "name" : medicine_name,
            "brand" : brand,
            "unit" : unit,
            "quantity" : quantity,
            "discount" : discount,
            "total" : total
        })
        
        grand_total += total
        
        # update stock in inventory dictionary
        if unit == "tablet":
            inventory[medicine_name][1] -= quantity
        elif unit == "strip":
            inventory[medicine_name][1] -= quantity * tablets_per_strip
    
    if len(purchased_items) > 0:
        print(f"\n Grand Total: Rs {grand_total:.2f}")
        update_inventory(file_path, inventory)
        generate_sales_invoice(customer_name, purchased_items, grand_total)
        print("\n Stock updated successfully.") 