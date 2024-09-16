import math


def s(x, tolerance=3e-8):
    sum = 0.0
    k = 1
    term1 = 1 / math.sqrt(k ** 3 + x)
    term2 = 1 / math.sqrt(k ** 3 - x)

    while max(term1, term2) >= tolerance:
        sum += term1 - term2
        k += 1
        term1 = 1 / math.sqrt(k ** 3 + x)
        term2 = 1 / math.sqrt(k ** 3 - x)

    return sum, k


def estimate_time(x):
    _, terms_needed = s(x)


def s_optimized(x, tolerance=3e-8):
    sum_result = 0.0
    k = 1
    term = ((math.sqrt(k ** 3 - x) - math.sqrt(k ** 3 + x))
            / math.sqrt(k ** 6 - x ** 2))

    while abs(term) >= tolerance:
        sum_result += term
        k += 1
        term = ((math.sqrt(k ** 3 - x) - math.sqrt(k ** 3 + x))
                / math.sqrt(k ** 6 - x ** 2))

    return sum_result, k


time_per_term = 500e-6
x_values = [0.5, 0.999999999]

for x in x_values:
    print(f"\nРезультат для x = {x}:")

    result, terms = s(x)
    print(f"s(x) = {result:.10f}, \nЧисло членов ряда: {terms}")

    total_time = terms * time_per_term
    print(f"Время выполнения {x}: {total_time:.6f} секунд")

    result_optimized, terms_optimized = s_optimized(x)
    print(f"s(x) (оптимизированный) = {result_optimized:.10f}, \nЧисло членов ряда: {terms_optimized}")

    total_time_optimized = terms_optimized * time_per_term
    print(f"Время выполнения {total_time_optimized:.6f} секунд")
