def get_multiplication_table(table_size):
    multiplication_table = []

    for i in range(1, table_size + 1):
        nested_array = [0 for _ in range(1, table_size + 1)]
        multiplication_table.append(nested_array)

    for i in range(table_size):
        for j in range(table_size):
            multiplication_table[i][j] = (i + 1) * (j + 1)

    return multiplication_table


user_table_size = int(input("Введите число, которое задает размер таблицы: "))

multiplication_table_list = get_multiplication_table(user_table_size)

for row in multiplication_table_list:
    print(*row)
