def search_element_in_list(list_to_search, umber_to_search):
    for i in range(len(list_to_search)):
        if int(list_to_search[i]) == umber_to_search:
            return i
    else:
        return -1


entered_list_to_search = input("Введите несколько числел через пробел, для создания списка: ").split()
entered_number_to_search = int(input("Введите число для поиска в созданном вами списке: "))

print(search_element_in_list(entered_list_to_search, entered_number_to_search))
