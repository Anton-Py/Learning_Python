import math

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

if abs(a - 0) >= 0.1:

    d = math.pow(b, 2) - (4 * a * c)

    if d < 0:
        print("Уравнение не имеет корней")
    elif d > 0:
        x_1 = (-b + math.sqrt(d)) / (2 * a)
        x_2 = (-b - math.sqrt(d)) / (2 * a)
        print(f'Уравнение имеет два корня. Корень первый: {x_1:.4f}, корень второй: {x_2:.4f}')
    elif d == 0:
        x = (-b + math.sqrt(d)) / 2 * a
        print(f"Уравнение имеет один корень. Корень: {x:.4f}")
else:
    print("Уравнение линейное")
    # if abs(a - 0) <= 0.1 and abs(b - 0) <= 0.1 and abs(c - 0) <= 0.1:
    #     print("Решением уравнения является: 0")
    if abs(b - 0) >= 0.1:
        x = (-c / b)
        print(f"Решением уравнения является: {x:.4f}")
    elif abs(b - 0) <= 0.1 and abs(c - 0) >= 0.1:
        print("Уравнение корней не имеет")
    elif abs(b - 0) <= 0.1 and abs(c - 0) <= 0.1:
        print("Корнем уравнения является любое число")
