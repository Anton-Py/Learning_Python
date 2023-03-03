day = int(input("Введите номер дня: "))
month = int(input("Введите сегодняшний месяц: "))
year = int(input("Введите сегодняшний год: "))

if month <= 0 or month > 12:
    print(f"Количество месяцев в году 12, вы ввели месяц {month}, введите корректную дату.")
else:
    if month == 4 or month == 6 or month == 9 or month == 11:
        days_in_month_quantity = 30
    elif month == 2:
        if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            days_in_month_quantity = 28
        else:
            days_in_month_quantity = 29
    else:
        days_in_month_quantity = 31

    if day <= 0 or day > days_in_month_quantity:
        print(f"Количество дней в веденном вами месяце {days_in_month_quantity},"
              f" вы ввели дней {day}, введите корректную дату.")
    elif day == days_in_month_quantity and month == 12:
        next_day = 1
        next_month = 1
        next_year = year + 1
        print(f"{next_day:0>2}.{next_month:0>2}.{next_year}")
    elif day == days_in_month_quantity:
        next_day = 1
        next_month = month + 1
        next_year = year
        print(f"{next_day:0>2}.{next_month:0>2}.{next_year}")
    else:
        next_day = day + 1
        next_month = month
        next_year = year
        print(f"{next_day:0>2}.{next_month:0>2}.{next_year}")
