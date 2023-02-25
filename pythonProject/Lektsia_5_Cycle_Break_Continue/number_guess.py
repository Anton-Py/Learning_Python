from random import randint

user_number = int(input("Введите число: "))

random_number = randint(1, 101)
attempts_quantity = 1

while True:
    if user_number == random_number:
        print(f"Вы отгадали число за {attempts_quantity} попыток")
        break

    if user_number > random_number:
        print("Загаданное число меньше")
        attempts_quantity += 1
    else:
        print("Загаданное число больше")
        attempts_quantity += 1

    user_number = int(input("Введите число: "))
