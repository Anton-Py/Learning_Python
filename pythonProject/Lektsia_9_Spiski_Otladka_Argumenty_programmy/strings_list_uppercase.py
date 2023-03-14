def change_list_to_uppercase(list_to_change):
    for i in range(len(list_to_change)):
        list_to_change[i] = list_to_change[i].upper()


entered_list_to_change = input("Введите несколько строк  через пробел для создания списка: ").split()

print(change_list_to_uppercase(entered_list_to_change))
