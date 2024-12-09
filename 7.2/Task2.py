import time

import matplotlib.pyplot as plt
import numpy as np

# Константы
alpha = 0.01


# Определение системы уравнений
def ecosystem(t, y):
    r, f = y
    drdt = 2 * r - alpha * r * f
    dfdt = -f + alpha * r * f
    return [drdt, dfdt]


# Реализация метода Рунге-Кутты 4-го порядка
def runge_kutta_4(f, t_span, y0, t_eval):
    t0, t_max = t_span
    n = len(t_eval)
    h = (t_max - t0) / (n - 1)

    t = t_eval
    y = np.zeros((n, len(y0)))
    y[0] = np.array(y0, dtype=float)  # Преобразуем y0 в numpy-массив с плавающей точкой

    for i in range(1, n):
        ti = t[i - 1]
        yi = y[i - 1]  # yi уже numpy-массив

        k1 = np.array(f(ti, yi))
        k2 = np.array(f(ti + h / 2, yi + h * k1 / 2))
        k3 = np.array(f(ti + h / 2, yi + h * k2 / 2))
        k4 = np.array(f(ti + h, yi + h * k3))

        y[i] = yi + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return t, y


# Функция для численного решения
def solve_system(r0, f0, t_max=50):
    t_span = (0, t_max)
    y0 = [r0, f0]
    t_eval = np.linspace(0, t_max, 5000)
    t, y = runge_kutta_4(ecosystem, t_span, y0, t_eval)
    return t, y


# Построение графиков поведения системы при различных начальных условиях
def plot_ecosystem(conditions, t_max=50):
    plt.figure(figsize=(12, 8))

    for r0, f0 in conditions:
        t, y = solve_system(r0, f0, t_max)  # Correctly unpack the result here
        plt.plot(t, y[:, 0], label=f"Rabbits r0={r0}, f0={f0}")
        plt.plot(t, y[:, 1], label=f"Foxes r0={r0}, f0={f0}", linestyle="--")

    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title("Dynamics of the Ecosystem")
    plt.legend()
    plt.grid()
    plt.show()


# Функция для вывода конечного результата и времени выполнения
def display_final_results(conditions, t_max=50):
    for r0, f0 in conditions:
        start_time = time.time()  # Начало замера времени
        t, y = solve_system(r0, f0, t_max)
        end_time = time.time()  # Конец замера времени

        elapsed_time = end_time - start_time
        final_r, final_f = y[-1]  # Конечные значения популяций

        print(f"Initial conditions: Rabbits={r0}, Foxes={f0}")
        print(f"Final state at t={t_max}: Rabbits={final_r:.2f}, Foxes={final_f:.2f}")
        print(f"Time taken: {elapsed_time:.4f} seconds")
        print("-" * 50)


# Исследование поведения системы при различных начальных условиях
if __name__ == "__main__":
    # Начальные условия для анализа
    initial_conditions = [
        (2, 3),  # Небольшое число кроликов и лис
        (15, 22),  # Среднее число кроликов и лис
        (1000, 2000),  # Очень большое начальное число кроликов и лис
    ]

    display_final_results(initial_conditions)

    # Исследование начальных условий, приводящих к вымиранию
    extinction_conditions = [
        (1, 100),  # Мало кроликов, много лис
        (15, 22),  # Среднее число кроликов и лис
        (0, 0),  # Полное отсутствие видов
    ]

    display_final_results(extinction_conditions)

    # Начальные условия для анализа
    initial_conditions = [
        (2, 3),  # Небольшое число кроликов и лис
        (15, 22),  # Число кроликов и лис среднего размера
        (1000, 2000),  # Очень большое начальное число кроликов и лис
    ]

    # Построение графиков для начальных условий
    plot_ecosystem(initial_conditions)

    # Исследование начальных условий, приводящих к вымиранию
    extinction_conditions = [
        (1, 100),  # Мало кроликов, много лис
        (15, 22),  # Число кроликов и лис среднего размера
        (0, 0),  # Полное отсутствие видов
    ]

    plot_ecosystem(extinction_conditions)
