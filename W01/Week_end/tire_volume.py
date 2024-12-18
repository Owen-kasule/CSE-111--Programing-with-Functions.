# tire_volume.py Author: Owen Kasule Muhereza

import math
from datetime import datetime

def calculate_tire_volume(width, aspect_ratio, diameter):
    """
    Calculate the approximate volume of a tire in liters.
    """
    volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
    return volume

def get_tire_price(width, aspect_ratio, diameter):
    """
    Retrieve the price for a tire based on width, aspect ratio, and diameter.
    """
    # Dictionary of predefined tire sizes and their prices
    tire_prices = {
        (185, 50, 14): 75.00,
        (205, 60, 15): 85.00,
        (215, 55, 16): 95.00,
        (225, 65, 17): 105.00,
        (235, 70, 18): 115.00
    }
    # Check if the entered size matches any in the predefined dictionary
    return tire_prices.get((width, aspect_ratio, diameter), None)

def main():
    # Prompt user for input with separate prompts for each value
    width = float(input("Enter the width of the tire in mm (e.g., 205): "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire (e.g., 60): "))
    diameter = float(input("Enter the diameter of the wheel in inches (e.g., 15): "))

    # Calculate the volume and round to two decimal places
    volume = calculate_tire_volume(width, aspect_ratio, diameter)
    print(f"The approximate volume is {volume:.2f} liters")

    # Get the price based on tire dimensions
    price = get_tire_price(width, aspect_ratio, diameter)
    if price is not None:
        print(f"The price for a tire with these dimensions is ${price:.2f}")
    else:
        print("Sorry, we don't have a price for this tire size.")

    # Ask if the user wants to purchase tires
    purchase = input("Would you like to purchase tires with these dimensions? (yes/no): ").strip().lower()
    phone_number = None
    if purchase == "yes":
        phone_number = input("Please enter your phone number for contact: ")

    # Get the current date in YYYY-MM-DD format
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Append the data to volumes.txt
    with open("volumes.txt", "a") as file:
        if phone_number:
            # Include phone number if the user wants to purchase
            print(f"{current_date}, {int(width)}, {int(aspect_ratio)}, {int(diameter)}, {volume:.2f}, {price:.2f}, {phone_number}", file=file)
        else:
            # Without phone number if no purchase
            print(f"{current_date}, {int(width)}, {int(aspect_ratio)}, {int(diameter)}, {volume:.2f}", file=file)

# Run the program
if __name__ == "__main__":
    main()