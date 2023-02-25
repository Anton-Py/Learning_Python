first_number = int(input("Введите начальное число: "))
last_number = int(input("Введите конечное число: "))

numbers_sum = 0
numbers_quantity = 0
even_numbers_sum = 0
even_numbers_quantity = 0

for i in range(first_number, last_number + 1):
    numbers_sum += i
    numbers_quantity += 1

    if i % 2 == 0:
        even_numbers_sum += i
        even_numbers_quantity += 1

numbers_arithmetic_average = numbers_sum / numbers_quantity
even_numbers_arithmetic_average = even_numbers_sum / even_numbers_quantity

print(f"Среднее арифметическое чисел: {numbers_arithmetic_average}")
print(f"Среднее арифметическое только четных чисел: {even_numbers_arithmetic_average}")
