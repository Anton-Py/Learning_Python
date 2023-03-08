from random import randint

user_number = int(input("Введите число: "))

random_number = randint(1, 100)
attempts_quantity = 0

while True:
    attempts_quantity += 1

    if user_number == random_number:
        print(f"Вы отгадали число за {attempts_quantity} попыток")
        break
    if user_number > random_number:
        print("Загаданное число меньше")
    else:
        print("Загаданное число больше")

    user_number = int(input("Введите число: "))
