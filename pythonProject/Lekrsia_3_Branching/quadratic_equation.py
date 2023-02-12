import math

a = float(input("Введите коэффициен a: "))
b = float(input("Введите коэффициен b: "))
c = float(input("Введите коэффициен c: "))

d = math.pow(b, 2) - (4 * a * c)

if a != 0:
    if d < 0:
        print("Уравнение не имеет корней")
    elif d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("Уравнение имеет два корня. Корень первый: {:.4f}, корень второй: {:.4f}".format(x1, x2))
    elif d == 0:
        x = (-b + math.sqrt(d)) / 2 * a
        print("Уравнение имеет один корень. Корень: {}".format(x))
else:
    print("Уравнение линейное")
