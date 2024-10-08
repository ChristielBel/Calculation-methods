import numpy as np
import matplotlib.pyplot as plt

# Матрица коэффициентов A и вектор свободных членов b
A = np.array([[12.14, 1.32, -0.78, -2.75],
              [-0.89, 16.75, 1.88, -1.55],
              [2.65, -1.27, -15.64, -0.64],
              [2.44, 1.52, 1.93, -11.43]])

b = np.array([14.78, -12.14, -11.65, 4.26])


# Функция для метода Якоби
def jacobi_method(A, b, x0, tol, max_iter):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = x0.copy()
    errors = []

    for i in range(max_iter):
        x_new = (b - np.dot(R, x)) / D
        error = np.linalg.norm(b - np.dot(A, x_new))
        errors.append(error)

        if error < tol:
            break

        x = x_new

    return x, errors


# Функция для метода Зейделя
def gauss_seidel_method(A, b, x0, tol, max_iter):
    x = x0.copy()
    n = len(b)
    errors = []

    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            sum1 = sum(A[i, j] * x_new[j] for j in range(i))
            sum2 = sum(A[i, j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum1 - sum2) / A[i, i]

        error = np.linalg.norm(b - np.dot(A, x_new))
        errors.append(error)

        if error < tol:
            break

        x = x_new

    return x, errors


# Начальное приближение, точность и максимальное число итераций
x0 = np.zeros(4)
x0_1 = np.array([1.0, 1.0, 1.0, 1.0])
x0_2 = np.array([-1.0, -1.0, -1.0, -1.0])
tol = 1e-6
max_iter = 1000

# Решение с помощью метода Якоби
jacobi_solution, jacobi_errors = jacobi_method(A, b, x0, tol, max_iter)
jacobi_solution_1, jacobi_errors_1 = jacobi_method(A, b, x0_1, tol, max_iter)
jacobi_solution_2, jacobi_errors_2 = jacobi_method(A, b, x0_2, tol, max_iter)

# Решение с помощью метода Зейделя
seidel_solution, seidel_errors = gauss_seidel_method(A, b, x0, tol, max_iter)
seidel_solution_1, seidel_errors_1 = gauss_seidel_method(A, b, x0_1, tol, max_iter)
seidel_solution_2, seidel_errors_2 = gauss_seidel_method(A, b, x0_2, tol, max_iter)

print("Метод Якоби для x0=0: ",jacobi_solution,len(jacobi_errors))
print("Метод Зейделя для x0=0: ",seidel_solution,len(seidel_errors))
print("Метод Якоби для x0=[1.0, 1.0, 1.0, 1.0]: ",jacobi_solution_1,len(jacobi_errors_1))
print("Метод Зейделя для x0=[1.0, 1.0, 1.0, 1.0]: ",seidel_solution_1,len(seidel_errors_1))
print("Метод Якоби для x0=[-1.0, -1.0, -1.0, -1.0]: ",jacobi_solution_2,len(jacobi_errors_2))
print("Метод Зейделя для x0=[-1.0, -1.0, -1.0, -1.0]: ",seidel_solution_2,len(seidel_errors_2))
# Построение графиков нормы невязки
plt.figure(figsize=(10, 6))
plt.plot(jacobi_errors, label='Jacobi Method (x0 = 0)', color='blue')
plt.plot(jacobi_errors_1, label='Jacobi Method (x0 = [1, 1, 1, 1])', color='cyan')
plt.plot(jacobi_errors_2, label='Jacobi Method (x0 = [-1, -1, -1, -1])', color='darkblue')
plt.plot(seidel_errors, label='Seidel Method (x0 = 0)', color='green')
plt.plot(seidel_errors_1, label='Seidel Method (x0 = [1, 1, 1, 1])', color='lime')
plt.plot(seidel_errors_2, label='Seidel Method (x0 = [-1, -1, -1, -1])', color='darkgreen')

plt.yscale('log')
plt.xlabel('Iteration')
plt.ylabel('Residual Norm')
plt.title('Convergence of Iterative Methods')
plt.legend()
plt.grid(True)
plt.show()

# Графики показывают, что при различных начальных значениях методы сходятся к одному и тому же решению,
# хотя скорость сходимости остается почти одинаковой для метода Зейделя.
