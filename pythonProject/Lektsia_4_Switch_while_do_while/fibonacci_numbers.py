fibonacci_number_index = int(input("Введите номер элемента ряда Фибоначчи: "))

previous_fibonacci_number = 0
current_fibonacci_number = 1

i = 0

while i < fibonacci_number_index:
    fibonacci_numbers_sum = previous_fibonacci_number + current_fibonacci_number
    previous_fibonacci_number = current_fibonacci_number
    current_fibonacci_number = fibonacci_numbers_sum

    i += 1

print(f"Число Фибоначчи с номером {fibonacci_number_index} =", previous_fibonacci_number)
