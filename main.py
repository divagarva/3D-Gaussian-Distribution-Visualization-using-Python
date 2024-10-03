import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a meshgrid for the 3D Gaussian
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Define mean and standard deviation
mean = 0
std_dev = 1

# 3D Gaussian distribution formula
z = (1 / (2 * np.pi * std_dev ** 2)) * np.exp(-((x - mean) ** 2 + (y - mean) ** 2) / (2 * std_dev ** 2))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Labeling
ax.set_title('3D Gaussian Distribution')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Probability Density')

plt.show()
