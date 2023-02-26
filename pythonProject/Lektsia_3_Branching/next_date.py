day = int(input("Введите номер дня недели на сегодня: "))
month = int(input("Введите сегодняшний месяц: "))
year = int(input("Введите сегодняшний год: "))

if month > 12 or month <= 0:
    print(f"Количество месяцев в году 12, вы ввели месяц {month}, введите корректную дату.")
else:
    if month == 4 or month == 6 or month == 9 or month == 11:
        days_quantity_in_month = 30
    elif month == 2:
        if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            days_quantity_in_month = 28
        else:
            days_quantity_in_month = 29
    else:
        days_quantity_in_month = 31

    if day > days_quantity_in_month or day <= 0:
        print(f"Количество дней в веденном вами месяце {days_quantity_in_month},"
              f" вы ввели дней {day}, введите корректную дату.")
    elif day == days_quantity_in_month and month == 12:
        next_day = 1
        next_month = 1
        next_year = year + 1
        print(f"{next_day:0>2}.{next_month:0>2}.{next_year}")
    elif day == days_quantity_in_month and month < 12:
        next_day = 1
        next_month = month + 1
        next_year = year
        print(f"{next_day:0>2}.{next_month:0>2}.{next_year}")
    else:
        next_day = day + 1
        next_month = month
        next_year = year
        print(f"{next_day:0>2}.{next_month:0>2}.{next_year}")
