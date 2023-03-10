def move_list_items(list_to_move):
    for i in range(1, len(list_to_move) // 2 + 1):
        list_to_move[i - 1], list_to_move[-i] = list_to_move[-i], list_to_move[i - 1]

    return list_to_move


entered_list_to_move = input("Введите данные через пробел, для формирования списка: ").split()

print(move_list_items(entered_list_to_move))
