
def water_column_height(tower_height, tank_height):
    """Calculate the water column height."""
    return tower_height + (3 * tank_height / 4)

def pressure_gain_from_water_height(height):
    """Calculate pressure gain from water height."""
    density = 998.2  # kg/m^3
    gravity = 9.80665  # m/s^2
    return (density * gravity * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculate pressure loss due to pipe friction."""
    density = 998.2  # kg/m^3
    return -((friction_factor * pipe_length * density * fluid_velocity**2) / (2000 * pipe_diameter))