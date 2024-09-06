def phi(x, tolerance=8e-5):
    sum_phi = 0.0
    k = 1
    while True:
        term = 1 / (k * (k + x))
        if term < tolerance:
            break
        sum_phi += term
        k += 1
    return sum_phi

# Вычисление для значений x от 0 до 1 с шагом 0.1
x_values = [i * 0.1 for i in range(11)]
results = {x: phi(x) for x in x_values}
for x, value in results.items():
    print(f"x = {x:.1f}, φ(x) = {value:.8f}")

def phi_faster(x, tolerance=8e-5):
    sum_phi = 0.0
    k = 1
    while True:
        term1 = 1 / (k * (k + x))
        term2 = 1 / (k * (k + x + 1))
        if abs(term1 - term2) < tolerance:
            break
        sum_phi += term1
        k += 1
    return sum_phi

# Вычисление для значений x от 0 до 1 с шагом 0.1
faster_results = {x: phi_faster(x) for x in x_values}
for x, value in faster_results.items():
    print(f"x = {x:.1f}, φ(x) (быстрее) = {value:.8f}")
