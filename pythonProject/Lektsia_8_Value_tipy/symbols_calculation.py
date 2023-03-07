def calculate_symbol(string):
    count_sting = 0
    count_digit = 0
    count_spase = 0
    count_other_symbol = 0

    for f in string:
        if f.isalpha():
            count_sting += 1
        elif f.isdigit():
            count_digit += 1
        elif f.isspace():
            count_spase += 1
        else:
            count_other_symbol += 1

    print(f"Количество букв в строке: {count_sting}\nКоличество цифр в строке {count_digit}\n"
          f"Количество пробельных символов в строке {count_spase}\n"
          f"Количество остальных символов {count_other_symbol}")


string_users = input("Введите строку: ")

calculate_symbol(string_users)
