fibonacci_number_series = int(input("Введите номер элемента ряда Фибоначчи: "))

number_1 = 0
number_2 = 1

count = 0

while count < fibonacci_number_series - 1:
    fibonacci_sum = number_1 + number_2
    number_1 = number_2
    number_2 = fibonacci_sum

    count += 1

print(f"Число Фибоначчи с номером {fibonacci_number_series} =", number_1)
