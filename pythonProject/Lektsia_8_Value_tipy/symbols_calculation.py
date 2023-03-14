def calculate_symbols(string):
    letters_quantity = 0
    digits_quantity = 0
    spaces_quantity = 0
    other_symbols_quantity = 0

    for symbol in string:
        if symbol.isalpha():
            letters_quantity += 1
        elif symbol.isdigit():
            digits_quantity += 1
        elif symbol.isspace():
            spaces_quantity += 1
        else:
            other_symbols_quantity += 1

    print(f"Количество букв в строке: {letters_quantity}\nКоличество цифр в строке {digits_quantity}\n"
          f"Количество пробельных символов в строке {spaces_quantity}\n"
          f"Количество остальных символов {other_symbols_quantity}")


user_string = input("Введите строку: ")

calculate_symbols(user_string)
