rectangle_length = float(input("Enter the length of the rectangle: "))
rectangle_width = float(input("Enter the width of the rectangle: "))

rectangle_area = rectangle_length * rectangle_width
rectangle_perimeter = 2 * (rectangle_length + rectangle_width)

print(f"Rectangle_length: {rectangle_length:.2f}, rectangle_width: {rectangle_width:.2f}, "
      f"rectangle_area: {rectangle_area:.2f}, rectangle_perimeter: {rectangle_perimeter:.2f}")
