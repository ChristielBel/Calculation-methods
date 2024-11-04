# Required libraries
import numpy as np
import matplotlib.pyplot as plt

# Constants for the problem
n = 4  # variant number
N = 100  # number of random points

# Define the function for the integrand for n <= 10
def f_integral(x):
    return np.sqrt(11 - n * (np.sin(x)) ** 2)

# Define the bounds for the rectangle
a = 5  # x-range [0, 5]
b = max(f_integral(np.linspace(0, a, 100)))  # Maximum y-value of the function

# Monte Carlo method for estimating the integral
x_random = np.random.uniform(0, a, N)
y_random = np.random.uniform(0, b, N)

# Count points under the curve
M = sum(1 for x, y in zip(x_random, y_random) if y < f_integral(x))

# Calculate the area estimate
integral_estimate = (M / N) * a * b

# Calculate error metrics
absolute_error = abs(integral_estimate - (b * a)) / N  # Approximate absolute error
relative_error = absolute_error / integral_estimate  # Relative error

# Plotting the function and random points
x_vals = np.linspace(0, a, 1000)
y_vals = f_integral(x_vals)

print(f"Интеграл: {integral_estimate:.6f}",f"\nАбсолютная погрешность: {absolute_error:.6f}",f"\nОтносительная погрешность: {relative_error:.6f}")

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="y = sqrt(11 - n * (sin(x))^2)", color="blue")
plt.scatter(x_random, y_random, color="orange", s=10, alpha=0.5, label="Random Points")
plt.fill_between(x_vals, y_vals, color="lightblue", alpha=0.3)
plt.xlim(0, a)
plt.ylim(0, b)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Monte Carlo Estimation of the Integral")
plt.legend()
plt.grid(True)
plt.show()
