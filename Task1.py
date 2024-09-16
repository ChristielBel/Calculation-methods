import math

def solve_quadratic_standard(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None 
    sqrt_discriminant = math.sqrt(discriminant)

    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)

    return x1, x2

def solve_quadratic_alternative(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None  
    sqrt_discriminant = math.sqrt(discriminant)

    if b > 0:
        x1 = (-b - sqrt_discriminant) / (2 * a)
        x2 = (2 * c) / (-b - sqrt_discriminant)
    else:
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (2 * c) / (-b + sqrt_discriminant)

    return x1, x2

def solve_vieta(a, b, c):
    if a == 0:
        return None, None 
    x1_plus_x2 = -b / a
    x1_times_x2 = c / a

    discriminant = x1_plus_x2 ** 2 - 4 * x1_times_x2
    if discriminant < 0:
        return None, None 

    sqrt_discriminant = math.sqrt(discriminant)
    x1 = (x1_plus_x2 + sqrt_discriminant) / 2
    x2 = (x1_plus_x2 - sqrt_discriminant) / 2

    return x1, x2

def get_coefficients():
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))
    return a, b, c

def main():
    a, b, c = get_coefficients()
    x1_standard, x2_standard = solve_quadratic_standard(a, b, c)
    x1_alternative, x2_alternative = solve_quadratic_alternative(a, b, c)
    x1_vieta, x2_vieta = solve_vieta(a, b, c)

    print("\nСтандартное решение:")
    if x1_standard is None:
        print("Уравнение не имеет вещественных корней.")
    else:
        print(f"x1 = {x1_standard}, x2 = {x2_standard}")

    print("\nАльтернативное решение:")
    if x1_alternative is None:
        print("Уравнение не имеет вещественных корней.")
    else:
        print(f"x1 = {x1_alternative}, x2 = {x2_alternative}")

    print("\nРешение по Виету:")
    if x1_vieta is None:
        print("Уравнение не имеет вещественных корней.")
    else:
        print(f"x1 = {x1_vieta}, x2 = {x2_vieta}")


if __name__ == "__main__":
    main()
