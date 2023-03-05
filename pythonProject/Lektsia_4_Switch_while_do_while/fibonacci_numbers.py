fibonacci_number_element = int(input("Введите номер элемента ряда Фибоначчи: "))

fibonacci_first_number = 0
fibonacci_second_number = 1

i = 0

while i < fibonacci_number_element:
    fibonacci_numbers_sum = fibonacci_first_number + fibonacci_second_number
    fibonacci_number_1 = fibonacci_second_number
    fibonacci_second_number = fibonacci_numbers_sum

    i += 1

print(f"Число Фибоначчи с номером {fibonacci_number_element} =", fibonacci_first_number)
