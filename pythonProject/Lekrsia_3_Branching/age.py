age = int(input("Введите свой возраст от 1 до 112 включительно: "))

remainder_years_division = age % 10

if age < 1:
    print("Вы слишком малы")
elif age > 112:
    print("Вы слишком стары")

if 11 <= age <= 14 or (age // 10 == (11 or 12 or 13)):
    print("Вам {} лет".format(age))
elif 2 <= remainder_years_division <= 4:
    print("Вам {} года".format(age))
elif remainder_years_division == 1:
    print("Вам {} год".format(age))
else:
    print("Вам {} лет".format(age))
