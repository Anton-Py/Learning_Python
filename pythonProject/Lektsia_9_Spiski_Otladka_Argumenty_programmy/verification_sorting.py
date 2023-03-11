def verification_string_to_increasing(list_to_verification):
    verification = True

    for i in range(len(list_to_verification) - 1):
        if list_to_verification[i] < list_to_verification[i + 1]:
            verification = True
        else:
            verification = False
            break

    if verification:
        return "Список отсортирован по возрастанию"
    else:
        return "Список отсортирован не по возрастанию"


def verification_string_to_declining(list_to_verification):
    verification = True

    for i in range(len(list_to_verification) - 1):
        if list_to_verification[i] > list_to_verification[i + 1]:
            verification = True
        else:
            verification = False
            break

    if verification:
        return "Список отсортирован по убыванию"
    else:
        return "Список отсортирован не по убыванию"


entered_list_to_verification = input("Введите несколько чисел через пробел для создания списка: ").split()

print(verification_string_to_increasing(entered_list_to_verification))
print(verification_string_to_declining(entered_list_to_verification))
