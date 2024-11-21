# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # m/s^2
WATER_DENSITY = 998.2                   # kg/m^3
WATER_DYNAMIC_VISCOSITY = 0.0010016     # Pa·s
KPA_TO_PSI_CONVERSION = 0.1450377377    # 1 kPa = 0.1450377377 psi

def water_column_height(tower_height, tank_height):
    """Calculate the water column height."""
    return tower_height + (3 * tank_height / 4)

def pressure_gain_from_water_height(height):
    """Calculate pressure gain from water height."""
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculate pressure loss due to pipe friction."""
    return -((friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2) / (2000 * pipe_diameter))

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculate the pressure loss from pipe fittings."""
    return -(0.04 * WATER_DENSITY * (fluid_velocity ** 2) * quantity_fittings) / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculate the Reynolds number."""
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calculate pressure loss due to pipe diameter reduction."""
    k = (0.1 + (50 / reynolds_number)) * (((larger_diameter / smaller_diameter) ** 4) - 1)
    return -(k * WATER_DENSITY * (fluid_velocity ** 2)) / 2000

def kpa_to_psi(kpa):
    """Convert pressure from kilopascals to pounds per square inch."""
    return kpa * KPA_TO_PSI_CONVERSION


# Constants for the pipeline system
PVC_SCHED80_INNER_DIAMETER = 0.28687  # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013   # (unitless)
SUPPLY_VELOCITY = 1.65                # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692  # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018    # (unitless)
HOUSEHOLD_VELOCITY = 1.75             # (meters / second)

def main():
    # Input from user
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    
    # Calculate water column height and initial pressure
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    
    # First pipeline segment
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    
    # Fitting losses
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    
    # Pipe reduction losses
    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    
    # Second pipeline segment
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    
    # Final pressure at house
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {kpa_to_psi(pressure):.2f} psi")

if __name__ == "__main__":
    main()
