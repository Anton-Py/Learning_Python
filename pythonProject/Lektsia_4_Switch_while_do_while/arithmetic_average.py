primary_number = int(input("Введите начальное число: "))
final_number = int(input("Введите конечное число: "))

numbers_sum = 0
number_quantity = 0
numbers_sum_even = 0
number_quantity_even = 0

for f in range(primary_number, final_number + 1):
    numbers_sum += f
    number_quantity += 1

    if f % 2 == 0:
        numbers_sum_even += f
        number_quantity_even += 1

arithmetic_average = numbers_sum / number_quantity
arithmetic_average_even_numbers = numbers_sum_even / number_quantity_even

print(f"Среднее арифметическое чисел: {arithmetic_average}")
print(f"Среднее арифметическое только четных чисел: {arithmetic_average_even_numbers}")
