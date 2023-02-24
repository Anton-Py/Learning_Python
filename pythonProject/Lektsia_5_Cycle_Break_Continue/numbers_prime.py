number_integer = int(input("Введите целое число: "))

for number in range(number_integer + 1):
    count = 0
    for number_digit in range(1, number + 1):
        if number % number_digit == 0:
            count += 1
    if count == 2:
        print(number, end=" ")
