import math

numbers_amount = int(input("Введите число: "))
row_sum = 0

for i in range(1, numbers_amount + 1):
    if i % 2 != 0:
        row_sum += math.pow(i, 2)
    else:
        row_sum -= math.pow(i, 2)

print("Сумма ряда:", row_sum)
