number_integer = int(input("Введите целое число для подсчета числа Фибоначи: "))

number_first = 1
sum_first_and_next_number = 0
count = 0

print(sum_first_and_next_number, end=' ')

for i in range(number_integer):
    sum_first_and_next_number = number_first + sum_first_and_next_number
    number_first = sum_first_and_next_number - number_first
    count += 1
    if count == number_integer - 1:
        print()
        print("Число Фибоначчи сномером n = ", sum_first_and_next_number)
