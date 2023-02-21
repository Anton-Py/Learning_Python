import math

amount_numbers = int(input("Введите число: "))
sum_row = 0

for f in range(1, amount_numbers + 1):
    if f % 2 != 0:
        sum_row += math.pow(f, 2)
    else:
        sum_row -= math.pow(f, 2)

print("Сумма ряда: ", sum_row)
