import math

x1, y1 = float(input("Введите координату x1: ")), float(input("Введите координату y1: "))
x2, y2 = float(input("Введите координату x2: ")), float(input("Введите координату y2: "))
x3, y3 = float(input("Введите координату x3: ")), float(input("Введите координату y3: "))

if 0.5 * ((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) == 0:
    print("Точки лежат на одной прямой, площадь треугольника вычисляться не будет")
else:
    a = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    c = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    semi_perimeter = (a + b + c) * 0.5
    triangle_area = math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))
    print("Area of a triangle:", triangle_area)
