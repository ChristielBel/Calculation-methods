import numpy as np
import matplotlib.pyplot as plt

# Constants for the problem
n = 15  # variant number
N = 100  # Number of random points

# Determine A and B based on n
A = n + 10 #там было =, так что не ебу + или -, но с + прикольнее
B = n - 10


# Define the polar equation in Cartesian coordinates
def p(phi):
    return np.sqrt((A * (np.cos(phi))**2 + B * (np.sin(phi))**2))

# Create values for phi
phi_values = np.linspace(0, 2 * np.pi, 1000)

# Get Cartesian coordinates of the curve
x_values = p(phi_values) * np.cos(phi_values)
y_values = p(phi_values) * np.sin(phi_values)

# Define rectangle dimensions [-a, a] x [-b, b]
a = np.max(np.abs(x_values))  # a is the max x value
b = np.max(np.abs(y_values))  # b is the max y value

# Generate random points in the rectangle
x_random = np.random.uniform(-a, a, N)
y_random = np.random.uniform(-b, b, N)

# Count points inside the figure
M = sum(1 for x, y in zip(x_random, y_random) if (x**2 / A + y**2 / B) < 1)

print("M={}".format(M))

# Calculate area approximation
area_estimate = (M / N) * (2 * a) * (2 * b)

print(f"Площадь фигуры: {area_estimate}")

# Plotting the figure and random points
plt.figure(figsize=(8, 8))
plt.plot(x_values, y_values, label="Boundary of the figure", color="blue")
plt.scatter(x_random, y_random, color="orange", s=10, alpha=0.5, label="Random Points")
plt.xlim(-a, a)
plt.ylim(-b, b)
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f"Monte Carlo Estimation of Area\nEstimated Area = {area_estimate:.4f}")
plt.legend()
plt.grid()
plt.show()
