import math
import time

# Точность для остановки суммирования
epsilon = 8e-3


# Функция для вычисления s(x)
def s(x, tolerance=epsilon):
    sum_positive = 0.0
    sum_negative = 0.0
    k = 1
    while True:
        term_positive = 1 / math.sqrt(k ** 3 + x)
        term_negative = 1 / math.sqrt(k ** 3 - x)

        # Суммирование для ряда с +x
        sum_positive += term_positive
        sum_negative += term_negative

        # Проверка на точность
        if max(term_positive, term_negative) < tolerance:
            break

        k += 1

    return sum_positive - sum_negative, k


# Оценка времени выполнения
def estimate_time(x, tolerance=epsilon):
    start_time = time.time()
    _, terms_needed = s(x, tolerance)
    end_time = time.time()

    # Время для одного слагаемого в микросекундах
    time_per_term = 500e-6  # 500 микросекунд

    total_time = terms_needed * 2 * time_per_term  # 2 ряда по одному числу
    print(f"Количество членов ряда: {terms_needed}")
    print(f"Оценочное время выполнения для x = {x}: {total_time:.6f} секунд")
    return total_time


# Применение оптимизированного метода для быстрого вычисления s(x)
def s_optimized(x, tolerance=epsilon):
    sum_result = 0.0
    k = 1
    while True:
        # Используем разложение Тейлора для более быстрого вычисления разности
        term = (2 * x) / (k ** (7 / 2))

        sum_result += term

        # Проверка на точность
        if abs(term) < tolerance:
            break

        k += 1

    return sum_result, k


# Тестируем для значений x = 0.5 и x = 0.999999999
x_values = [0.5, 0.999999999]

for x in x_values:
    print(f"\nРезультат для x = {x}:")

    # Стандартный метод
    result, terms = s(x)
    print(f"s(x) (обычный метод) = {result:.10f}, Число членов ряда: {terms}")

    # Оценка времени
    estimate_time(x)

    # Оптимизированный метод
    result_optimized, terms_optimized = s_optimized(x)
    print(f"s(x) (оптимизированный метод) = {result_optimized:.10f}, Число членов ряда: {terms_optimized}")
