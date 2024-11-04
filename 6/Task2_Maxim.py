# Required libraries
import numpy as np
import matplotlib.pyplot as plt

# Constants for the problem
n = 15  # variant number for the integral computation
N = 100  # number of random points for Monte Carlo integration

# Define the function for the integral based on n
def f_integral(x):
    return (29 - n * (np.cos(x))**2)**0.5

# Determine rectangle bounds for the graph
a = 5  # Upper limit of integration
b = max(f_integral(np.linspace(0, a, 100)))  # Maximum value of f_integral in [0, 5]

# Monte Carlo method for integral approximation
x_random = np.random.uniform(0, a, N)
y_random = np.random.uniform(0, b, N)

# Count points under the curve
M = sum(1 for x, y in zip(x_random, y_random) if y < f_integral(x))

# Calculate the integral approximation
integral_estimate = (M / N) * a * b

# Calculate error metrics
absolute_error = abs(integral_estimate - (a * b)) / N  # Approximate absolute error
relative_error = absolute_error / integral_estimate  # Relative error

# Plotting the function and random points
x_vals = np.linspace(0, a, 1000)
y_vals = [f_integral(x) for x in x_vals]

print(f"Интеграл: {integral_estimate:.6f}",f"\nАбсолютная погрешность: {absolute_error:.6f}",f"\nОтносительная погрешность: {relative_error:.6f}")

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="y = f_integral(x)", color="blue")
plt.scatter(x_random, y_random, color="orange", s=10, alpha=0.5, label="Random Points")
plt.fill_between(x_vals, y_vals, color="lightblue", alpha=0.3)
plt.xlim(0, a)
plt.ylim(0, b)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Monte Carlo Integration Approximation")
plt.legend()
plt.grid(True)
plt.show()
