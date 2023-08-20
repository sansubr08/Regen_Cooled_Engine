#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt

# Parameters
# Define parameters as needed for your specific simulation

# Number of iterations
iterations = 100

# Initialize arrays that store results
T_wall = np.zeros(iterations)
T_cool = np.zeros(iterations)

# Initial conditions
T_wall[0] = 600  # K (initial wall temperature) - change this
T_cool[0] = 20  # K (initial coolant temperature)#t_cool_inlet - change this

# Simulation loop
for i in range(1, iterations):
    # Flow Equations
    # Calculate mass flow rate
    rho = 1.0  # Placeholder density - change this
    A_channel = 0.1  # Placeholder cross-sectional area - change this
    V_gas = 100  # Placeholder gas velocity - change this
    mdot = rho * A_channel * V_gas
    cp = 100 #assigning random value
   
    # Pressure Drop
    f = 0.02  # Placeholder Darcy friction factor for demonstration
    L_channel = 1.0  # Placeholder channel length for demonstration
    D_hydraulic = 0.05  # Placeholder hydraulic diameter for demonstration
    delta_P = f * (L_channel / D_hydraulic) * (rho * V_gas**2) / 2
   
    # Heat Transfer Equations
    # Heat Flux to Wall
    h = 2000  # Placeholder convective heat transfer coefficient for demonstration
    T_gas = 3000  # Placeholder gas temperature for demonstration
    q_gas_to_wall = h * (T_gas - T_wall[i-1])
   
    # Heat Flux to Coolant
    A_wall = 0.1  # Placeholder wall area - change this
    mdot_coolant = 1.67  # Placeholder coolant mass flow rate - change this
    q_wall_to_coolant = (q_gas_to_wall * A_wall) / mdot_coolant
   
    # Update Temperatures
    # Update wall temperature
    T_wall[i] = T_wall[i-1] + (q_wall_to_coolant / (mdot_coolant * cp * A_wall))
   
    # Update coolant temperature
    q_gas_to_wall_per_mdot = q_gas_to_wall / mdot_coolant
    T_cool[i] = T_cool[i-1] + ((q_gas_to_wall_per_mdot - q_wall_to_coolant) / cp)

# Plot results
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(range(iterations), T_wall, 'r', linewidth=2)
plt.xlabel('Iterations')
plt.ylabel('Wall Temperature (K)')
plt.title('Regenerative Cooling Simulation')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(range(iterations), T_cool, 'b', linewidth=2)
plt.xlabel('Iterations')
plt.ylabel('Coolant Temperature (K)')
plt.grid(True)

plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:




