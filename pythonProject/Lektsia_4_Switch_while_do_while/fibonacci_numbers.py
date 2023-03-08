fibonacci_number_index = int(input("Введите номер элемента ряда Фибоначчи: "))

fibonacci_previous_number = 0
fibonacci_next_number = 1

i = 0

while i < fibonacci_number_index:
    fibonacci_numbers_sum = fibonacci_previous_number + fibonacci_next_number
    fibonacci_previous_number = fibonacci_next_number
    fibonacci_next_number = fibonacci_numbers_sum

    i += 1

print(f"Число Фибоначчи с номером {fibonacci_number_index} =", fibonacci_previous_number)
