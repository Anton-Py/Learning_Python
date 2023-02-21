import math

x_1 = float(input("Введите координату x1: "))
y_1 = float(input("Введите координату y1: "))
x_2 = float(input("Введите координату x2: "))
y_2 = float(input("Введите координату y2: "))
x_3 = float(input("Введите координату x3: "))
y_3 = float(input("Введите координату y3: "))

epsilon = 0.0001

if abs((x_1 - x_3) * (y_2 - y_3) - (x_2 - x_3) * (y_1 - y_3)) <= epsilon:
    print("Точки лежат на одной прямой, площадь треугольника вычисляться не будет")
else:
    a = math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
    b = math.sqrt((x_1 - x_3) ** 2 + (y_1 - y_3) ** 2)
    c = math.sqrt((x_3 - x_2) ** 2 + (y_3 - y_2) ** 2)

    semi_perimeter = (a + b + c) * 0.5
    triangle_area = math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))
    print("Area of a triangle:", triangle_area)
