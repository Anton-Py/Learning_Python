seed_number = int(input("Введите первоначальное число: "))
finite_number = int(input("Введите конечное число: "))

amount_numbers = 0
number_values = 0
amount_numbers_even_number = 0
number_values_even_number = 0

for f in range(seed_number, finite_number + 1):
    amount_numbers += f
    number_values += 1

    if f % 2 == 0:
        amount_numbers_even_number += f
        number_values_even_number += 1

arithmetic_average = amount_numbers / number_values
arithmetic_average_even_number = amount_numbers_even_number / number_values_even_number

print(f"Среднее арифметическое чисел: {arithmetic_average}")
print(f"Среднее арифметическое только четных чисел: {arithmetic_average_even_number}")
