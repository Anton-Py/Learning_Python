# area of a triangle
a = 4
b = 6
c = 3

semi_perimeter = 0.5 * (a + b + c)
triangle_area = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5

print("Area of a triangle:", triangle_area)
