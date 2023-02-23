day = int(input("Введите день недели: "))
month = int(input("Введите сегодняшний месяц: "))
year = int(input("Введите сегодняшний год: "))

if month > 12:
    print(f"Количество месяцев в году 12, вы ввели месяц {month}, введите корректную дату.")
elif len(str(year)) != 4:
    print(f"Вы ввели не корректный год {year}, введите корректную дату.")

if month == 4 or month == 6 or month == 9 or month == 11:
    day_in_month = 30
elif month == 2:
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        day_in_month = 28
    else:
        day_in_month = 29
else:
    day_in_month = 31

if day > day_in_month:
    print(f"Количество дней в веденном вами месяце {day_in_month}, вы ввели дней {day}, введите корректную дату.")

if day == day_in_month and month == 12:
    final_day = 1
    final_month = 1
    final_year = year + 1
elif day == day_in_month and month < 12:
    final_day = 1
    final_month = month + 1
    final_year = year
else:
    final_day = day + 1
    final_month = month
    final_year = year

print(f"{final_day:0>2}.{final_month:0>2}.{final_year}")
