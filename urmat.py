import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


def explicit_scheme(dx, dt, T, L):
    Nx = int(L / dx) + 1
    Nt = int(T / dt) + 1

    x = np.linspace(0, L, Nx)
    t = np.linspace(0, T, Nt)

    u = np.zeros((Nt, Nx))

    # Начальное условие
    u[0, :] = np.sin(x)

    # Граничные условия
    u[:, 0] = 0
    u[:, -1] = np.exp(-t)

    r = dt / dx ** 2

    # Явная разностная схема
    for n in range(0, Nt - 1):
        for i in range(1, Nx - 1):
            u[n + 1, i] = u[n, i] + r * (u[n, i + 1] - 2 * u[n, i] + u[n, i - 1])

    return x, t, u


def implicit_scheme(dx, dt, T, L):
    Nx = int(L / dx) + 1
    Nt = int(T / dt) + 1

    x = np.linspace(0, L, Nx)
    t = np.linspace(0, T, Nt)

    u = np.zeros((Nt, Nx))

    # Начальное условие
    u[0, :] = np.sin(x)

    # Граничные условия
    u[:, 0] = 0
    u[:, -1] = np.exp(-t)

    r = dt / dx ** 2

    # Матрица для неявной схемы
    A = np.zeros((Nx - 2, Nx - 2))
    np.fill_diagonal(A, 1 + 2 * r)
    np.fill_diagonal(A[:-1, 1:], -r)
    np.fill_diagonal(A[1:, :-1], -r)

    for n in range(0, Nt - 1):
        b = u[n, 1:-1]
        b[0] += r * u[n + 1, 0]
        b[-1] += r * u[n + 1, -1]
        u[n + 1, 1:-1] = np.linalg.solve(A, b)

    return x, t, u


def exact_solution(x, t):
    return np.exp(-t)[:, None] * np.sin(x)


def print_results_table(x, u_explicit, u_implicit, u_exact, t_idx):
    print(f"\nРезультаты на временном шаге t = {t_idx}:")
    headers = ["x", "Явная схема", "Неявная схема", "Точное решение"]
    table = []
    for i in range(len(x)):
        table.append(
            [f"{x[i]:.4f}", f"{u_explicit[t_idx, i]:.4f}", f"{u_implicit[t_idx, i]:.4f}", f"{u_exact[t_idx, i]:.4f}"])
    print(tabulate(table, headers=headers, tablefmt="grid", numalign="center", stralign="center"))


def plot_results(x, t, u_explicit, u_implicit, u_exact):
    T_idx = len(t) - 1  # Последний временной шаг

    plt.figure(figsize=(10, 6))
    plt.plot(x, u_explicit[T_idx, :], label='Явная схема', marker='o')
    plt.plot(x, u_implicit[T_idx, :], label='Неявная схема', marker='x')
    plt.plot(x, u_exact[T_idx, :], label='Точное решение', linestyle='--')

    plt.xlabel('x')
    plt.ylabel('u(x, t)')
    plt.title(f'Сравнение решений на последнем временном шаге t = {t[-1]:.2f}')
    plt.legend()
    plt.grid()
    plt.show()


def get_user_input():
    try:
        L = float(input("Введите длину области L (по умолчанию: pi/2): ") or (np.pi / 2))
        T = float(input("Введите время T (по умолчанию: 1.0): ") or 1.0)
        dx = float(input("Введите шаг по пространству dx (по умолчанию: 0.1): ") or 0.1)
        dt = float(input("Введите шаг по времени dt (по умолчанию: 0.005): ") or 0.005)
        return L, T, dx, dt
    except ValueError:
        print("Некорректный ввод. Используются значения по умолчанию.")
        return np.pi / 2, 1.0, 0.1, 0.005


def main():
    # Ввод параметров
    print("Добро пожаловать в решатель уравнения теплопроводности.")
    L, T, dx, dt = get_user_input()

    x, t, u_explicit = explicit_scheme(dx, dt, T, L)
    x, t, u_implicit = implicit_scheme(dx, dt, T, L)
    u_exact = exact_solution(x, t)

    # Вывод результатов в консоль в виде таблицы
    print_results_table(x, u_explicit, u_implicit, u_exact, len(t) - 1)

    # Построение графиков результатов
    plot_results(x, t, u_explicit, u_implicit, u_exact)


if __name__ == "__main__":
    main()
