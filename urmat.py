import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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
    if r > 0.5:
        raise ValueError("Схема нестабильна! Уменьшите dt или увеличьте dx.")

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
    if r > 0.5:
        raise ValueError("Схема нестабильна! Уменьшите dt или увеличьте dx.")

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


def run_solution():
    try:
        L = float(entry_L.get())
        T = float(entry_T.get())
        dx = float(entry_dx.get())
        dt = float(entry_dt.get())

        x, t, u_explicit = explicit_scheme(dx, dt, T, L)
        x, t, u_implicit = implicit_scheme(dx, dt, T, L)
        u_exact = exact_solution(x, t)

        T_idx = len(t) - 1  # Индекс последнего временного шага

        # Очищаем старую таблицу
        for row in tree.get_children():
            tree.delete(row)

        # Заполняем таблицу результатами
        for i in range(len(x)):
            tree.insert("", "end", values=(f"{x[i]:.4f}",
                                           f"{u_explicit[T_idx, i]:.4f}",
                                           f"{u_implicit[T_idx, i]:.4f}",
                                           f"{u_exact[T_idx, i]:.4f}"))

        # Строим график
        plot_results(x, t, u_explicit, u_implicit, u_exact)
    except ValueError:
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные значения.")


# Создаем главное окно
root = tk.Tk()
root.title("Решатель уравнения теплопроводности")

# Ввод параметров
frame_input = ttk.LabelFrame(root, text="Параметры")
frame_input.grid(row=0, column=0, padx=10, pady=10)

ttk.Label(frame_input, text="Длина области L:").grid(row=0, column=0, padx=5, pady=5)
entry_L = ttk.Entry(frame_input)
entry_L.grid(row=0, column=1, padx=5, pady=5)
entry_L.insert(0, str(np.pi / 2))

ttk.Label(frame_input, text="Время T:").grid(row=1, column=0, padx=5, pady=5)
entry_T = ttk.Entry(frame_input)
entry_T.grid(row=1, column=1, padx=5, pady=5)
entry_T.insert(0, "1.0")

ttk.Label(frame_input, text="Шаг по x (dx):").grid(row=2, column=0, padx=5, pady=5)
entry_dx = ttk.Entry(frame_input)
entry_dx.grid(row=2, column=1, padx=5, pady=5)
entry_dx.insert(0, "0.1")

ttk.Label(frame_input, text="Шаг по t (dt):").grid(row=3, column=0, padx=5, pady=5)
entry_dt = ttk.Entry(frame_input)
entry_dt.grid(row=3, column=1, padx=5, pady=5)
entry_dt.insert(0, "0.005")

# Кнопка для запуска решения
btn_run = ttk.Button(root, text="Запустить решение", command=run_solution)
btn_run.grid(row=1, column=0, padx=10, pady=10)

# Таблица для отображения результатов
frame_table = ttk.LabelFrame(root, text="Результаты")
frame_table.grid(row=2, column=0, padx=10, pady=10)

columns = ("x", "Явная схема", "Неявная схема", "Точное решение")
tree = ttk.Treeview(frame_table, columns=columns, show="headings")
tree.grid(row=0, column=0, padx=5, pady=5)

for col in columns:
    tree.heading(col, text=col)

root.mainloop()
