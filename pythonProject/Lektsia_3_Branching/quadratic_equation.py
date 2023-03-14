import math

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

epsilon = 0.0001

if abs(a) > epsilon:  # a != 0
    discriminant = math.pow(b, 2) - (4 * a * c)

    if discriminant > epsilon:  # d > 0
        x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f'Уравнение имеет два корня. Корень первый: {x_1:.4f}, корень второй: {x_2:.4f}')
    elif abs(discriminant) <= epsilon:  # d == 0
        x = -b / (2 * a)
        print(f"Уравнение имеет один корень. Корень: {x:.4f}")
    else:  # d < 0
        print("Уравнение не имеет корней")

elif abs(b) > epsilon:  # b != 0
    x = -c / b
    print(f"Решением уравнения является: {x:.4f}")
elif abs(c) <= epsilon:  # b == 0 c == 0
    print("Корнем уравнения является любое число")
else:  # b == 0 c != 0
    print("Уравнение корней не имеет")
