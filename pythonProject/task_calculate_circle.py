import math

# площадь круга и длина окружности с заданным радиусом

circle_radius = 5

circle_area = math.pi * math.pow(circle_radius, 2)
print("Circle_area:", circle_area)

circumference = 2 * math.pi * circle_radius
print("Circumference:", circumference)

# радиус окружности с заданной площадью круга

circle_area = 16

circle_radius = math.sqrt(circle_area / math.pi)
print("Circle_radius:", circle_radius)

# площадь сектора с заданными радиусом и углом в градусах

circumference = 10
corner = 120

sector_area = math.pi/360 * math.pow(circumference, 2) * corner
print("Sector_area:", sector_area)
