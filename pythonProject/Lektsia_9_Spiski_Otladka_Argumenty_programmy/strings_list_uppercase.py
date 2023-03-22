def convert_list_to_uppercase(strings_list):
    for i in range(len(strings_list)):
        strings_list[i] = strings_list[i].upper()


entered_strings_list = input("Введите несколько строк через пробел для создания списка: ").split()

convert_list_to_uppercase(entered_strings_list)
