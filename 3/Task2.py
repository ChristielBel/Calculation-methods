import math

import numpy as np

def erf(x):
    def integrand(t):
        return (2 / np.sqrt(np.pi)) * np.exp(-t**2)

    n = 10000
    a = 0
    b = x
    h = (b - a) / n
    integral = 0.5 * (integrand(a) + integrand(b))

    for i in range(1, n):
        integral += integrand(a + i * h)

    integral *= h
    return integral

# Матрица коэффициентов
A = np.array([[1.00, 0.80, 0.64],
              [1.00, 0.90, 0.81],
              [1.00, 1.10, 1.21]])

# Вектор правых частей (значения erf)
b = np.array([erf(0.80), erf(0.90), erf(1.10)])

A2 = np.array([[0.1, 0.2, 0.3],
               [0.4, 0.5, 0.6],
               [0.7, 0.8, 0.9]])

b2 = np.array([0.1, 0.3, 0.5])




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


import numpy as np

def row_echelon_form(matrix):
    A = np.copy(matrix)
    rows, cols = A.shape
    row = 0

    for col in range(cols):
        if row >= rows:
            break

        max_row = np.argmax(np.abs(A[row:rows, col])) + row
        A[[row, max_row]] = A[[max_row, row]]

        if A[row, col] == 0:
            continue

        for r in range(row + 1, rows):
            factor = A[r, col] / A[row, col]
            A[r] -= factor * A[row]

        row += 1

    return A


def matrix_rank(matrix):
    echelon_form = row_echelon_form(np.array(matrix))
    rank = np.sum(np.any(np.abs(echelon_form) > 1e-10, axis=1))
    return rank


rank_A = matrix_rank(A)
print("Ранг матрицы A:", rank_A)
print("Число обусловленности:", np.linalg.cond(A))

# Проверка существования решений
if rank_A < min(A.shape):
    print("Система имеет множество решений")
else:
    print("Система имеет единственное решение")
    x = gaussian_elimination_with_pivoting(A, b)
    print("Решение:", x)
    sum = 0
    for i in range(3):
        sum+=x[i]
    print("Сумма x1,x2,x3:",sum)
    print("Erf(1.0):",erf(1))

print()

rank_A2 = matrix_rank(A2)
print("Ранг матрицы A2:", rank_A2)
print("Число обусловленности:", np.linalg.cond(A2))

# Проверка существования решений
if rank_A2 < min(A2.shape):
    print("Система имеет множество решений")
else:
    print("Система имеет единственное решение")
    x = gaussian_elimination_with_pivoting(A2, b2)
    print("Решение:", x)
