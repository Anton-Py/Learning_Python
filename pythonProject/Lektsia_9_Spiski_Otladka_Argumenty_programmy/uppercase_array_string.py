def change_uppercase_line(list_to_change):
    for i in range(len(list_to_change)):
        list_to_change[i] = list_to_change[i].upper()

    return list_to_change


entered_list_to_change = input("Введите несколько строк  через пробел для создания списка: ").split()

print(change_uppercase_line(entered_list_to_change))
