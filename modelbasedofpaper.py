#!/usr/bin/env python
# coding: utf-8

# In[15]:


''''import numpy as np
import matplotlib.pyplot as plt

# Constants
n = 0.4  # Prandtl number exponent
cp = 1000  # Specific heat capacity of coolant (J/kg K)

# Parameters
iterations = 100
dx = 0.01  # Discretization step
L = 1.0  # Length of the wall (m)
A = 0.1  # Cross-sectional area of the channel (m^2)
D = 0.05  # Hydraulic diameter (m)
k = 100  # Thermal conductivity (W/m K)
Re = 1000  # Reynolds number
Pr = 0.7  # Prandtl number (for example)
Ti = 600  # Initial wall temperature (K)
Tc_inlet = 20  # Initial coolant inlet temperature (K)

# Initialize arrays to store results
T_wall = np.zeros(iterations)
T_coolant = np.zeros(iterations)

T_wall[0] = Ti
T_coolant[0] = Tc_inlet

# Simulation loop


# Simulation loop
for i in range(1, iterations - 1):  # Adjusted iteration range
    # Calculate heat transfer coefficient using the given formula
    h = (0.023 * k**0.8 * Re**0.8 * Pr**n) / D
    
    # Update wall temperature using finite difference method
    dTdx2 = (T_wall[i-1] - 2 * T_wall[i] + T_wall[i+1]) / dx**2
    T_wall[i] = T_wall[i-1] - Q * dx / (cp * mdot_coolant * A) - dTdx2
    
    # Update coolant temperature
    T_coolant[i] = T_coolant[i-1] + (Q / (mdot_coolant * cp))

''''for i in range(1, iterations):
    # Calculate heat transfer coefficient using the given formula
    h = (0.023 * k**0.8 * Re**0.8 * Pr**n) / D
    
   # Calculate heat transfer rate
    Q = h * A * (T_wall[i-1] - T_coolant[i-1])
    
    # Update wall temperature using finite difference method
    dTdx2 = (T_wall[i-1] - 2 * T_wall[i] + T_wall[i+1]) / dx**2
    T_wall[i] = T_wall[i-1] - Q * dx / (cp * mdot_coolant * A) - dTdx2
    
    # Update coolant temperature
    T_coolant[i] = T_coolant[i-1] + (Q / (mdot_coolant * cp))'''
    
# Plot results
plt.figure(figsize=(10, 6))
plt.plot(range(iterations), T_wall, 'r', label='Wall Temperature')
plt.plot(range(iterations), T_coolant, 'b', label='Coolant Temperature')
plt.xlabel('Iterations')
plt.ylabel('Temperature (K)')
plt.title('Regenerative Cooling Simulation')
plt.legend()
plt.grid(True)
plt.show()


# In[14]:


import numpy as np
import matplotlib.pyplot as plt

# Constants
n = 0.4  # Prandtl number exponent
cp = 1000  # Specific heat capacity of coolant (J/kg K)

# Parameters
iterations = 100
dx = 0.01  # Discretization step
L = 1.0  # Length of the wall (m)
A = 0.1  # Cross-sectional area of the channel (m^2)
D = 0.05  # Hydraulic diameter (m)
k = 100  # Thermal conductivity (W/m K)
Re = 1000  # Reynolds number
Pr = 0.7  # Prandtl number (for example)
Ti = 600  # Initial wall temperature (K)
Tc_inlet = 20  # Initial coolant inlet temperature (K)
mdot_coolant = 1.67  # Placeholder coolant mass flow rate for demonstration

# Initialize arrays to store results
T_wall = np.zeros(iterations)
T_coolant = np.zeros(iterations)

T_wall[0] = Ti
T_coolant[0] = Tc_inlet

# Simulation loop
for i in range(1, iterations - 1):
    # Calculate heat transfer coefficient using the given formula
    h = (0.023 * k**0.8 * Re**0.8 * Pr**n) / D
    
    # Calculate heat transfer rate
    Q = h * A * (T_wall[i-1] - T_coolant[i-1])
    
    # Update wall temperature using finite difference method
    dTdx2 = (T_wall[i-1] - 2 * T_wall[i] + T_wall[i+1]) / dx**2
    T_wall[i] = T_wall[i-1] - Q * dx / (cp * mdot_coolant * A) - dTdx2
    
    # Update coolant temperature
    T_coolant[i] = T_coolant[i-1] + (Q / (mdot_coolant * cp))

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(range(iterations), T_wall, 'r', label='Wall Temperature')
plt.plot(range(iterations), T_coolant, 'b', label='Coolant Temperature')
plt.xlabel('Iterations')
plt.ylabel('Temperature (K)')
plt.title('Regenerative Cooling Simulation')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




