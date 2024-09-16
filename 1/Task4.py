import math

const1 = math.pi ** 2 / 6
const2 = math.pi ** 4 / 90


def series(tolerance=1e-10):
    sum_remainder = 0.0
    n = 1
    term = 1 / (n ** 4 * (n ** 2 + 1))

    while term >= tolerance:
        sum_remainder += term
        n += 1
        term = 1 / (n ** 4 * (n ** 2 + 1))

    return const1 - const2 + sum_remainder


result = series()
print(f"Сумма ряда: {result:.10f}")
