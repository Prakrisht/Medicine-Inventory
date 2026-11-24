import datetime

def generate_sales_invoice(customer_name, purchased_items, total_amount):
    """
    Generates a VAT invoice as a .txt file for a customer sale transaction.
    The file name is unique based on the customer name and current timestamp.

    Args:
        customer_name (str): The name of the customer.
        purchased_items (list): A list of dictionaries where each dictionary contains
                                name, brand, unit, quantity, discount, and total.
        total_amount (float): The grand total cost of all purchased items.

    Returns:
        None
    """
    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d_%H-%M-%S")
    invoice_file_name = f"Invoice_{customer_name}_{date_string}.txt"
    
    try:
        with open(invoice_file_name, "w") as file:
            file.write("=" * 93 + "\n")
            file.write("        MEDSTORE PVT. LTD. -  VAT INVOICE\n")
            file.write("=" * 93 + "\n")
            file.write(f"Customer Name: {customer_name}\n")
            file.write(f"Date & Time : {date_string}\n")
            file.write("-" * 93 + "\n")
            file.write(f"{'S.No.':<6} {'Medicine':<20} {'Brand':<18} {'Unit':<8} {'Quantity':>10} {'Discount':>12} {'Total':>12}\n")
            file.write("-" * 93 + "\n")
            
            sn = 1
            for item in purchased_items:
                file.write(
                    f"{sn:<6} "
                    f"{item['name']:<20} "
                    f"{item['brand']:<18} "
                    f"{item['unit']:<8} "
                    f"{item['quantity']:>10} "
                    f"{item['discount']:>12.2f} "
                    f"{item['total']:>12.2f}\n"
                )
                sn += 1
        
            file.write("-" * 93 + "\n")
            file.write(f"{'Total Amount':>60} Rs {total_amount:.2f}\n")
            file.write("=" * 93 + "\n")
        print(f"Invoice generated successfully: {invoice_file_name}")
    except Exception as e:
        print(f"Error generating invoice: {e}")
        
def generate_restock_note(supplier_name, restocked_items, total_amount):
    """
    Generates a restock note as a .txt file for a supplier restock transaction.
    The file name is unique based on the supplier name and current timestamp.

    Args:
        supplier_name (str): The name of the supplier.
        restocked_items (list): A list of dictionaries where each dictionary contains
                                name, brand, unit, quantity, rate, and total.
        total_amount (float): The grand total cost of all restocked items.

    Returns:
        None
    """
    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d_%H-%M-%S")
    note_file_name = f"Restock_Note_{supplier_name}_{date_string}.txt"
    
    try:
        with open(note_file_name, "w") as file:
            file.write("=" * 93 + "\n")
            file.write("        MEDSTORE PVT. LTD. -  RESTOCK NOTE\n")
            file.write("=" * 93 + "\n")
            file.write(f"Supplier Name: {supplier_name}\n")
            file.write(f"Date & Time : {date_string}\n")
            file.write("-" * 93 + "\n")
            file.write(f"{'S.No.':<6} {'Medicine':<20} {'Brand':<18} {'Unit':<8} {'Quantity':>10} {'Rate/Unit':>12} {'Total':>12}\n")
            file.write("-" * 93 + "\n")
            
            sn = 1
            for item in restocked_items:
                file.write(
                    f"{sn:<6} "
                    f"{item['name']:<20} "
                    f"{item['brand']:<18} "
                    f"{item['unit']:<8} "
                    f"{item['quantity']:>10} "
                    f"{item['rate']:>12.2f} "
                    f"{item['total']:>12.2f}\n"
                )
                sn += 1
                
            file.write("-" * 93 + "\n")
            file.write(f"{'Total Amount':>60} Rs {total_amount:.2f}\n")
            file.write("=" * 93 + "\n")
        print(f"Restock note generated successfully: {note_file_name}")
    except Exception as e:
        print(f"Error generating restock note: {e}")