age = int(input("Введите свой возраст от 1 до 112 включительно: "))

if age < 1:
    print("Вы слишком малы")
elif age > 112:
    print("Вы слишком стары")
else:
    if 11 <= age <= 14 or (age // 10 == (11 or 12 or 13)):
        print("лет")
    elif 2 <= age % 10 <= 4:
        print("года")
    elif age % 10 == 1:
        print("год")
    else:
        print("лет")

