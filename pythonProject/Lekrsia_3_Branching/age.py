age = int(input("Введите свой возраст от 1 до 112 включительно: "))

age_last_digit = age % 10
age_last_two_digits = age % 100

if age < 1:
    print("Вы слишком малы")
elif age > 112:
    print("Вы слишком стары")
else:
    if age_last_digit == 1 and age_last_two_digits != 11:
        print(f"Вам {age} год")
    elif 2 <= age_last_digit <= 4 and (age_last_two_digits < 10 or age_last_two_digits >= 20):
        print(f"Вам {age} года")
    else:
        print(f"Вам {age} лет")
