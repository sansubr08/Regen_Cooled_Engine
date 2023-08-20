#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_locations = 100  # Number of axial locations 
num_temperatures = 5  # Number of wall temperatures 
T_wall_uniform = np.array([540, 750, 1000, 1250, 1500])  # Uniform wall temperatures in R
T_wall_uniform_K = T_wall_uniform * (5/9)  # Convert to K

# Generate simulated data for StUeeρ (Stanton number-based variable)
# This data should be generated based on your actual simulation results
# You would replace this with actual data from TDK's output 
stuee_data = np.random.rand(num_locations, num_temperatures)

# Interpolation function for StUeeρ
interpolated_stuee = np.zeros((num_locations, num_temperatures))

# Perform interpolation for StUeeρ
for i in range(num_temperatures):
    interpolated_stuee[:, i] = np.interp(np.linspace(0, 1, num_locations), 
                                         np.linspace(0, 1, len(stuee_data)), stuee_data[:, i])

# Plot interpolated StUeeρ for each wall temperature
plt.figure(figsize=(8, 6))
for i in range(num_temperatures):
    plt.plot(np.linspace(0, 1, num_locations), interpolated_stuee[:, i], label=f'Wall Temp: {T_wall_uniform[i]} K')

plt.xlabel('Normalized Axial Location')
plt.ylabel('Interpolated StUeeρ')
plt.title('Interpolated StUeeρ at Different Wall Temperatures')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:




