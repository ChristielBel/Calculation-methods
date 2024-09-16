def phi(x, tolerance=0.5e-8):
    sum_phi = 0.0
    k = 1
    term = 1 / (k * (k + x))

    while term >= tolerance:
        sum_phi += term
        k += 1
        term = 1 / (k * (k + x))

    return sum_phi


x_values = [i * 0.1 for i in range(11)]
results = {x: phi(x) for x in x_values}
for x, value in results.items():
    print(f"x = {x:.1f}, φ1(x) = {value:.8f}")


def phi_faster(x, tolerance=0.5e-8):
    sum_phi = 0.0
    k = 1
    term1 = 1 / (k * (k + x))
    term2 = 1 / (k * (k + 1))

    while abs(term1 - term2) >= tolerance:
        sum_phi += term1 - term2
        k += 1
        term1 = 1 / (k * (k + x))
        term2 = 1 / (k * (k + 1))

    return sum_phi


faster_results = {x: phi_faster(x) for x in x_values}
for x, value in faster_results.items():
    print(f"x = {x:.1f}, φ2(x) = {value:.8f}")
