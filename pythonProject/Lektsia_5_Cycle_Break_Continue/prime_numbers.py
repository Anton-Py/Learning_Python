user_number = int(input("Введите целое число: "))

print("Все простые числа, которые содержит целое число:", end=" ")

for number in range(2, user_number + 1):
    is_prime_number = True

    for value in range(2, number):
        if number % value == 0:
            is_prime_number = False
            break

    if is_prime_number:
        print(number, end=" ")
