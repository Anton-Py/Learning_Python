def get_element_index(list_to_search, number_to_search):
    for i in range(len(list_to_search)):
        if int(list_to_search[i]) == number_to_search:
            return i

    return -1


entered_list_to_search = [int(i) for i in input("Введите несколько чисел через пробел, для создания списка:").split()]
entered_number_to_search = int(input("Введите число для поиска в созданном вами списке: "))

print(get_element_index(entered_list_to_search, entered_number_to_search))
