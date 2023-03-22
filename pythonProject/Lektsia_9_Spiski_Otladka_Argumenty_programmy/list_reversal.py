def reverse_items_list(list_for_reversal):
    for i in range(1, len(list_for_reversal) // 2 + 1):
        list_for_reversal[i - 1], list_for_reversal[-i] = list_for_reversal[-i], list_for_reversal[i - 1]


entered_list_for_reversal = input("Введите данные через пробел, для формирования списка: ").split()

reverse_items_list(entered_list_for_reversal)
