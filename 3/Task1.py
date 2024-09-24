import numpy as np


def gaussian_elimination_with_pivoting(A, b):
    n = len(b)

    for i in range(n):
        max_row = i + np.argmax(np.abs(A[i:n, i]))
        if i != max_row:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]

        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x


def calculate_residuals(A, b, x):
    residuals = b - np.dot(A, x)
    return residuals


# A = np.array([[1e-4, 1], [1, 2]], dtype=float)
# b = np.array([1, 4], dtype=float)

# A = np.array([[2.34, -4.21,-11.61], [8.04, 5.22,0.27], [3.92,-7.99,8.37]], dtype=float)
# b = np.array([14.41,-6.44, 55.56], dtype=float)

A = np.array([[4.43, -7.21, 8.05, 1.23, -2.56], [-1.29, 6.47, 2.96, 3.22, 6.12], [6.12, 8.31, 9.41, 1.78, -2.88],
              [-2.57, 6.93, -3.74, 7.41, 5.55], [1.46, 3.62, 7.83, 6.25, -2.35]], dtype=float)
b = np.array([2.62, -3.97, -9.12, 8.11, 7.23], dtype=float)

x = gaussian_elimination_with_pivoting(A.copy(), b.copy())

residuals = calculate_residuals(A, b, x)

print("Решение системы (x1, x2):", x)
print("Невязки:", residuals)
