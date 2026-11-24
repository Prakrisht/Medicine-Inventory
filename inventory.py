file_path = "medicine_inventory.txt"

def read_medicine_data(file_path):
    """
    Reads medicine inventory data from a text file and stores it in a dictionary.

    Args:
        file_path (str): The path to the medicine inventory text file.

    Returns:
        dict: A dictionary where the key is the medicine name and
              the value is a list of [brand, quantity, rate_tablet, rate_strip, tablets_per_strip].
    """
    inventory = {} # empty dictionary to store inventory data
    try:
        with open(file_path, "r") as file:
            lines = file.readlines() # read all lines at once from the file
            for line in lines:
                line = line.strip() # remove leading/trailing whitespace
                items = line.split(",") # split line by comma
                
                # validate that line has exactly 6 items
                if len(items) != 6:
                    print(f"Error: Invalid line in file {file_path}: {line}")
                    continue
                
                # extract each field from items and list
                medicine_name = items[0].strip()
                medicine_brand = items[1].strip()
                quantity_in_stock = int(items[2].strip())
                rate_per_tablet= float(items[3].strip())
                rate_per_strip = float(items[4].strip())
                tablets_per_strip = int(items[5].strip())

                # store in inventory dictionary with medicine name as key and list of details as value
                inventory[medicine_name] = [medicine_brand, quantity_in_stock, rate_per_tablet, rate_per_strip, tablets_per_strip]
                
    except FileNotFoundError:
        print(f"Error: File {file_path} could not be found.")
    except ValueError:
        print(f"Error: Invalid data in file {file_path}.")
    return inventory

def display_inventory(inventory):
    """
    Displays all medicines in the inventory in a formatted table in the Python shell.

    Args:
        inventory (dict): The dictionary containing all medicine records.

    Returns:
        None
    """
    
    print("=" * 119)
    print(f"| {'S.No.':<6} | {'Medicine ':<25} | {'Brand':<20} | {'Quantity':>10} | {'Rate/Tablet':>12} | {'Rate/Strip':>11} | {'Tablets/Strip':>13} |")
    print("=" * 119)

    sn = 1
    for name, details in inventory.items():
        print(f"| {sn:<6} | {name:<25} | {details[0]:<20} | {details[1]:>10} | {details[2]:>12.2f} | {details[3]:>11.2f} | {details[4]:>13} |")
        sn += 1
    print("=" * 119)

def update_inventory(file_path, inventory):
    """
    Overwrites the inventory text file with updated stock values after each transaction.

    Args:
        file_path (str): The path to the medicine inventory text file.
        inventory (dict): The updated dictionary containing all medicine records.

    Returns:
        None
    """
    try:
        with open(file_path, "w") as file:
            for name, details in inventory.items():
                # write each medicine record as a line in the file in the same format as original
                line = f"{name},{details[0]},{details[1]},{details[2]},{details[3]},{details[4]}\n"
                file.write(line)
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")

