#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

# Constants and parameters
chamber_length = 1.0  # Length of the combustion chamber (m)
coolant_channel_length = 0.1  # Length of each coolant channel (m)
num_channels = int(chamber_length / coolant_channel_length)

# Geometry and dimensions
chamber_inner_radius = 0.05  # Inner radius of the chamber (m)
chamber_outer_radius = 0.055  # Outer radius of the chamber (m)
coolant_channel_width = 0.005  # Width of each coolant channel (m)

# Material properties
wall_thickness = chamber_outer_radius - chamber_inner_radius  # Wall thickness (m)
wall_conductivity = 400  # Thermal conductivity of the chamber wall material (W/mK)
coolant_specific_heat = 4200  # Specific heat capacity of the coolant (J/kgK)
coolant_density = 800  # Coolant density (kg/m^3)
coolant_velocity = 5  # Coolant velocity (m/s)

# Heat transfer coefficients
gas_side_heat_transfer_coeff = 2000  # Gas-side heat transfer coefficient (W/m^2K)
coolant_side_heat_transfer_coeff = 8000  # Coolant-side heat transfer coefficient (W/m^2K)

# Gas temperature and heat flux
gas_temperature = 3000  # Initial gas temperature (K)
heat_flux = gas_side_heat_transfer_coeff * (gas_temperature - 300)  # Initial heat flux (W/m^2)

# Create an array to store wall temperatures
wall_temperatures = np.zeros(num_channels)
wall_temperatures[0] = gas_temperature  # Initial wall temperature is the same as gas temperature

# Perform the heat transfer calculations along the chamber
for i in range(1, num_channels):
    # Calculate the temperature change on the gas side
    delta_temperature_gas = (heat_flux / (2 * np.pi * chamber_inner_radius * coolant_channel_length * wall_thickness) -
                            (gas_temperature - wall_temperatures[i - 1])) / (gas_side_heat_transfer_coeff *
                                                                               wall_thickness)

    # Update the gas temperature
    gas_temperature -= delta_temperature_gas

    # Calculate the temperature change on the coolant side
    delta_temperature_coolant = (heat_flux / (coolant_side_heat_transfer_coeff * coolant_channel_width * coolant_channel_length) -
                                 (wall_temperatures[i - 1] - wall_temperatures[i])) / (coolant_specific_heat *
                                                                                         coolant_density *
                                                                                         coolant_velocity *
                                                                                         coolant_channel_width)

    # Update the wall temperature
    wall_temperatures[i] = wall_temperatures[i - 1] + delta_temperature_coolant

# Plot the temperature distribution along the chamber
x_positions = np.linspace(0, chamber_length, num_channels)
plt.plot(x_positions, wall_temperatures, label='Wall Temperature')
plt.xlabel('Distance Along Chamber (m)')
plt.ylabel('Temperature (K)')
plt.legend()
plt.grid(True)
plt.title('Temperature Distribution Along the Chamber Wall')
plt.show()


# In[ ]:





# In[ ]:




