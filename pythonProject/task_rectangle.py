rectangle_length = float(input("Введите длину прямоугольника: "))
rectangle_width = float(input("Введите ширину прямоугольника: "))

rectangle_area = rectangle_length * rectangle_width

rectangle_perimeter = 2 * (rectangle_length + rectangle_width)

print(f"rectangle_length: {rectangle_length}, rectangle_width: {rectangle_width}, "
      f"rectangle_area: {rectangle_area:.2f}, rectangle_perimeter: {rectangle_perimeter:.2f}")
