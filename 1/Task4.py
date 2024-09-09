import math

def compute_sum(tolerance=1e-10):
    sum_s = 0.0
    n = 1
    while True:
        term = 1 / (n**2 + 1)
        sum_s += term
        if term < tolerance:
            break
        n += 1

    # Корректируем остаток на больших n
    sum_s += (math.pi**2 / 6 - sum_s)  # Остаток суммы как разность между известной суммой и накопленной
    return sum_s

# Вычисляем сумму
result = compute_sum()
print(f"Сумма ряда = {result:.10f}")
