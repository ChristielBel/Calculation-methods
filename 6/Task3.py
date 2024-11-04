import numpy as np
import matplotlib.pyplot as plt

# Constants for the problem
n = 4  # variant number
R = n  # Radius of the circle
N = 100  # Number of random points

# Generate random points in the square [-R, R] x [-R, R]
x_random = np.random.uniform(-R, R, N)
y_random = np.random.uniform(-R, R, N)

# Count points that fall inside the circle
M = sum(1 for x, y in zip(x_random, y_random) if (x**2 + y**2) < R**2)

# Calculate the approximation of pi
pi_estimate = 4 * (M / N)

# Circle parameterization for plotting
theta = np.linspace(0, 2 * np.pi, 100)
circle_x = R * np.cos(theta)
circle_y = R * np.sin(theta)

print(f"PI: {pi_estimate}")

# Plotting the square and the circle with random points
plt.figure(figsize=(8, 8))
plt.plot(circle_x, circle_y, label="Circle of radius R", color="blue")
plt.scatter(x_random, y_random, color="orange", s=10, alpha=0.5, label="Random Points")
plt.xlim(-R, R)
plt.ylim(-R, R)
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f"Monte Carlo Estimation of Pi\nEstimated π = {pi_estimate:.4f}")
plt.legend()
plt.grid()
plt.show()
