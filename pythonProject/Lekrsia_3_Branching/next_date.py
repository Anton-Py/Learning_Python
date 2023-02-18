day = int(input("Ведите сегодняшний день недели: "))
month = int(input("Введите сегодняшний месяц: "))
year = int(input("Введите сегодняшний год: "))

single_year = year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)
cancel_printing = True

if month > 12:
    print(f"Количество месяцев в году 12, вы ввели месяц {month}, введите корректную дату.")
    cancel_printing = False
elif len(str(year)) != 4:
    print(f"Вы ввели не корректный год {year}, введите корректную дату.")
    cancel_printing = False

if month == 4 or month == 6 or month == 9 or month == 11:
    day_in_month = 30
elif month == 2:
    if single_year:
        day_in_month = 28
    else:
        day_in_month = 29
else:
    day_in_month = 31

if day > day_in_month:
    print(f"Количество дней в веденном вами месяце {day_in_month}, вы ввели дней {day}, введите корректную дату.")
    cancel_printing = False

if day == day_in_month:
    final_day = 1
    if month == 12:
        final_month = 1
        final_year = year + 1
    else:
        final_month = month + 1
        final_year = year
else:
    final_day = day + 1
    final_month = month
    final_year = year

if cancel_printing:
    if final_day < 10:
        if final_month < 10:
            print(f"0{final_day}.0{final_month}.{final_year}")
        else:
            print(f"0{final_day}.{final_month}.{final_year}")
    elif final_month < 10:
        if final_day < 10:
            print(f"0{final_day}.0{final_month}.{final_year}")
        else:
            print(f"{final_day}.0{final_month}.{final_year}")
    else:
        print(f"{final_day}.{final_month}.{final_year}")
