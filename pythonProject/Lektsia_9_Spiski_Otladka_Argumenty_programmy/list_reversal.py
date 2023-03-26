def reverse(list_for_reversal):
    for i in range(1, len(list_for_reversal) // 2 + 1):
        list_for_reversal[i - 1], list_for_reversal[-i] = list_for_reversal[-i], list_for_reversal[i - 1]


entered_list_for_reversal = input("Введите данные через пробел, для формирования списка: ").split()

reverse(entered_list_for_reversal)
print(entered_list_for_reversal)
