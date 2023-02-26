start_number = int(input("Введите начальное число: "))
end_number = int(input("Введите конечное число: "))
numbers_per_line_quantity = int(input("Введите количество чисел в строке: "))

current_numbers_per_line_quantity = 0
length_end_number = len(str(end_number))

for i in range(start_number, end_number + 1):
    current_numbers_per_line_quantity += 1
    print(f"{i: >{length_end_number}}", end=" ")

    if current_numbers_per_line_quantity == numbers_per_line_quantity:
        print()
        current_numbers_per_line_quantity = 0
