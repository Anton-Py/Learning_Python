number_users = int(input("Введите целое число: "))

print("Все простые числа, которые содержит целое число:", end=" ")

for number in range(2, number_users + 1):
    simple = True

    for digit in range(2, number):
        if number % digit == 0:
            simple = False

    if simple:
        print(number, end=" ")
