import math

def compute_volume(radius, height):
    """Calculate the volume of a cylinder."""
    return math.pi * radius ** 2 * height

def compute_surface_area(radius, height):
    """Calculate the surface area of a cylinder."""
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(volume, surface_area):
    """Calculate the storage efficiency of a cylinder."""
    return volume / surface_area

def compute_cost_efficiency(volume, cost):
    """Calculate the cost efficiency of a cylinder."""
    return volume / cost

def main():
    # Data for each can size
    cans = [
        {"name": "#1 Picnic", "radius": 6.83, "height": 10.16, "cost": 0.28},
        {"name": "#1 Tall", "radius": 7.78, "height": 11.91, "cost": 0.43},
        {"name": "#2", "radius": 8.73, "height": 11.59, "cost": 0.45},
        {"name": "#2.5", "radius": 10.32, "height": 11.91, "cost": 0.61},
        {"name": "#3 Cylinder", "radius": 10.79, "height": 17.78, "cost": 0.86},
        {"name": "#5", "radius": 13.02, "height": 14.29, "cost": 0.83},
        {"name": "#6Z", "radius": 5.40, "height": 8.89, "cost": 0.22},
        {"name": "#8Z short", "radius": 6.83, "height": 7.62, "cost": 0.26},
        {"name": "#10", "radius": 15.72, "height": 17.78, "cost": 1.53},
        {"name": "#211", "radius": 6.83, "height": 12.38, "cost": 0.34},
        {"name": "#300", "radius": 7.62, "height": 11.27, "cost": 0.38},
        {"name": "#303", "radius": 8.10, "height": 11.11, "cost": 0.42}
    ]

    # Track the best can sizes for storage and cost efficiency
    best_storage_efficiency = 0
    best_cost_efficiency = 0
    best_storage_can = ""
    best_cost_can = ""

    # Loop through each can and calculate its efficiencies
    for can in cans:
        volume = compute_volume(can["radius"], can["height"])
        surface_area = compute_surface_area(can["radius"], can["height"])
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        cost_efficiency = compute_cost_efficiency(volume, can["cost"])

        # Print the storage efficiency
        print(f"{can['name']}: Storage Efficiency = {storage_efficiency:.2f}")

        # Update best storage efficiency if applicable
        if storage_efficiency > best_storage_efficiency:
            best_storage_efficiency = storage_efficiency
            best_storage_can = can["name"]

        # Print the cost efficiency
        print(f"{can['name']}: Cost Efficiency = {cost_efficiency:.2f}")

        # Update best cost efficiency if applicable
        if cost_efficiency > best_cost_efficiency:
            best_cost_efficiency = cost_efficiency
            best_cost_can = can["name"]

    # Display the best can for each efficiency
    print("\nBest Storage Efficiency Can:", best_storage_can, f"with {best_storage_efficiency:.2f}")
    print("Best Cost Efficiency Can:", best_cost_can, f"with {best_cost_efficiency:.2f}")

# Run the main function
if __name__ == "__main__":
    main()
