age = int(input("Введите свой возраст от 1 до 112 включительно: "))

last_digit_age_1 = age % 10
last_digit_age_2 = age % 100

if age < 1:
    print("Вы слишком малы")
elif age > 112:
    print("Вы слишком стары")
else:
    if last_digit_age_1 == 1 and last_digit_age_1 != 11:
        print(f"Вам {age} год")
    elif 2 <= last_digit_age_1 <= 4 and (last_digit_age_2 < 10 or last_digit_age_2 >= 20):
        print(f"Вам {age} года")
    else:
        print(f"Вам {age} лет")
