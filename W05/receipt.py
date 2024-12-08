"""
Receipt Program
- Prints the store name at the top of the receipt.
- Prints a list of products requested by the customer.
- Includes additional functionality: Prints a reminder of how many days remain until New Year’s Day.
- Handles FileNotFoundError and KeyError with informative error messages.
- Contains at least one try block, and all statements that might raise exceptions are within try blocks or user-defined functions called within a try block.
- Prints the current date and time in the format specified in the assignment.
- Prints a thank you message near the bottom of the receipt.
- Computes and prints the correct total.
- **Additional Creativity**: Wishes the client a Merry Christmas and a Happy New Year with their name, heart ❤️ and smile 😊 emojis, and a small cash gift!
"""

import csv
from datetime import datetime, timedelta

def load_products(filename):
    """Load products from a CSV file and return a dictionary."""
    products = {}
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                product_id, name, price = row
                products[product_id] = {"name": name, "price": float(price)}
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the file name and try again.")
        raise
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'. Please check the file permissions.")
        raise
    return products

def load_requests(filename):
    """Load customer requests from a CSV file and return a list of dictionaries."""
    requests = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                product_id, quantity = row
                requests.append({"product_id": product_id, "quantity": int(quantity)})
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the file name and try again.")
        raise
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'. Please check the file permissions.")
        raise
    return requests

def calculate_receipt(products, requests):
    """Calculate and print the receipt."""
    store_name = "Inkom Emporium"
    sales_tax_rate = 0.06
    subtotal = 0
    total_items = 0
    client_name = "Valued Customer"
    holiday_gift = 5.00  # Small cash gift for the client
    
    print(store_name)
    print("=" * len(store_name))
    
    try:
        for request in requests:
            product_id = request["product_id"]
            quantity = request["quantity"]
            
            if product_id not in products:
                raise KeyError(f"Error: Unknown product ID in the request.csv file: '{product_id}'")
            
            product = products[product_id]
            name = product["name"]
            price = product["price"]
            item_total = price * quantity
            subtotal += item_total
            total_items += quantity
            
            print(f"{name}: {quantity} @ {price:.2f} = {item_total:.2f}")
        
        sales_tax = subtotal * sales_tax_rate
        total = subtotal + sales_tax
        
        print(f"\nNumber of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        
        # Print the current date and time in the specified format
        current_date_and_time = datetime.now()
        print(f"\nThank you for shopping at the {store_name}.")
        print(f"{current_date_and_time:%a %b %d %I:%M:%S %p %Y}")
        
        # Additional Functionality: Days until New Year’s Day
        new_year = datetime(current_date_and_time.year + 1, 1, 1)
        days_until_new_year = (new_year - current_date_and_time).days
        print(f"Reminder: Only {days_until_new_year} days until New Year's Day!")
        
        # Holiday Greeting and Small Gift
        print(f"\n🎄 Merry Christmas and a Happy New Year, {client_name}! ❤️😊")
        print(f"Here's a small holiday gift for you: ${holiday_gift:.2f}")
        
    except KeyError as e:
        print(e)
        raise

# Main Program
def main():
    products_file = "products.csv"
    requests_file = "request.csv"
    
    try:
        products = load_products(products_file)
        requests = load_requests(requests_file)
        calculate_receipt(products, requests)
    except (FileNotFoundError, KeyError) as e:
        print("An error occurred while processing the receipt. Please address the issues and try again.")

if __name__ == "__main__":
    main()
