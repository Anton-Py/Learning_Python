def is_list_sorted_by_ascending(list_to_verification):
    for i in range(len(list_to_verification) - 1):
        if list_to_verification[i] >= list_to_verification[i + 1]:
            return False

    return True


def is_list_sorted_by_descending(list_to_verification):
    for i in range(len(list_to_verification) - 1):
        if list_to_verification[i] <= list_to_verification[i + 1]:
            return False

    return True


entered_list_to_verification = [int(i) for i in
                                input("Введите несколько чисел через пробел для создания списка: ").split()]

print(is_list_sorted_by_ascending(entered_list_to_verification))
print(is_list_sorted_by_descending(entered_list_to_verification))
