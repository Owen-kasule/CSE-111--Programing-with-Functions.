# tire_volume.py Authors: Owen Kasule Muhereza

import math

def calculate_tire_volume(width, aspect_ratio, diameter):
    # Formula for the volume of space inside a tire in liters
    volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
    return volume

def main():
    # Get user input
    width = float(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

    # Calculate the volume
    volume = calculate_tire_volume(width, aspect_ratio, diameter)

    # Display the result
    print(f"The approximate volume is {volume:.2f} liters")

# Call the main function
main()