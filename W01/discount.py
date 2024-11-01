from datetime import datetime

# Define sales tax rate
SALES_TAX_RATE = 0.06
DISCOUNT_RATE = 0.10
DISCOUNT_THRESHOLD = 50.00
DISCOUNT_DAYS = {1, 2}  # Tuesday (1) and Wednesday (2)

# Get the current day of the week (0=Monday, ..., 6=Sunday)
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

# Get the subtotal amount from the user
subtotal = float(input("Please enter the subtotal: "))

# Check if discount applies (subtotal >= 50 and day is Tuesday or Wednesday)
if subtotal >= DISCOUNT_THRESHOLD and day_of_week in DISCOUNT_DAYS:
    discount_amount = subtotal * DISCOUNT_RATE
    subtotal -= discount_amount
    print(f"Discount amount: {discount_amount:.2f}")

# Calculate sales tax and total
sales_tax = subtotal * SALES_TAX_RATE
total = subtotal + sales_tax

# Print the results
print(f"Sales tax amount: {sales_tax:.2f}")
print(f"Total: {total:.2f}")
from datetime import datetime

# Define sales tax rate
SALES_TAX_RATE = 0.06
DISCOUNT_RATE = 0.10
DISCOUNT_THRESHOLD = 50.00
DISCOUNT_DAYS = {1, 2}  # Tuesday (1) and Wednesday (2)

# Get the current day of the week (0=Monday, ..., 6=Sunday)
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
#day_of_week = 1  # Adjust to 1-based index
# Get the subtotal amount from the user
subtotal = float(input("Please enter the subtotal: "))

# Check if discount applies (subtotal >= 50 and day is Tuesday or Wednesday)
if subtotal >= DISCOUNT_THRESHOLD and day_of_week in DISCOUNT_DAYS:
    discount_amount = subtotal * DISCOUNT_RATE
    subtotal -= discount_amount
    print(f"Discount amount: {discount_amount:.2f}")

# Calculate sales tax and total
sales_tax = subtotal * SALES_TAX_RATE
total = subtotal + sales_tax

# Print the results
print(f"Sales tax amount: {sales_tax:.2f}")
print(f"Total: {total:.2f}")