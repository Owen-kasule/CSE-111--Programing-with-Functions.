import math

EARTH_GRAVITY_ACCELERATION = 9.80665
Water_density = 998.2
DYNAMIC_VISCOSITY = 0.0010016 


def water_column_height(tower_height, tank_height):
   return tower_height + (tank_height*3)/4 

def pressure_gain_from_water_height(height):
 return (Water_density * EARTH_GRAVITY_ACCELERATION *height )/1000

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity): 
  return  (-friction_factor * pipe_length * Water_density * fluid_velocity**2)/  (2000 * pipe_diameter)

def  pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
  return (-0.04 * Water_density * fluid_velocity**2 * quantity_fittings )/2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
  return (Water_density * hydraulic_diameter * fluid_velocity )/ DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
  Diameter_ratio = larger_diameter / smaller_diameter
  K = (0.1 + 50 / reynolds_number) * (Diameter_ratio**4 - 1)
  return (-K * Water_density * fluid_velocity **2)/2000

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
if __name__ == "__main__":
    main()