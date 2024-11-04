import numpy as np
import matplotlib.pyplot as plt

n = 4
N = 100  # number of random points

def f(x):
    if x < n:
        return 10 * x / n
    elif x <= 20:
        return 10 * (x - 20) / (n - 20)
    else:
        return 0

a = 20  # Maximum x-range
b = max([f(x) for x in np.linspace(0, 20, 100)])  # Maximum y-range

x_random = np.random.uniform(0, a, N)
y_random = np.random.uniform(0, b, N)

M = sum(1 for x, y in zip(x_random, y_random) if y < f(x))

area_estimate = (M / N) * a * b

absolute_error = abs(area_estimate - (a * b)) / N  # absolute error
relative_error = absolute_error / area_estimate  # relative error

x_vals = np.linspace(0, a, 1000)
y_vals = [f(x) for x in x_vals]

print(f"Площадь фигуры: {area_estimate:.6f}",f"\nАбсолютная погрешность: {absolute_error:.6f}",f"\nОтносительная погрешность: {relative_error:.6f}")

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="y = f(x)", color="blue")
plt.scatter(x_random, y_random, color="orange", s=10, alpha=0.5, label="Random Points")
plt.fill_between(x_vals, y_vals, color="lightblue", alpha=0.3)
plt.xlim(0, a)
plt.ylim(0, b)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Monte Carlo Estimation of Triangle Area")
plt.legend()
plt.grid(True)
plt.show()
