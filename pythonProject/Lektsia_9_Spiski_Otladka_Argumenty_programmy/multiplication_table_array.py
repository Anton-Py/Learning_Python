def get_multiplication_table(table_size):
    multiplication_table = []

    for i in range(1, table_size + 1):
        nested_array = [0] * table_size
        multiplication_table.append(nested_array)

    for i in range(table_size):
        for j in range(table_size):
            multiplication_table[i][j] = (i + 1) * (j + 1)

    return multiplication_table


user_table_size = int(input("Введите число, которое задает размер таблицы: "))
end_number = len(str(user_table_size ** 2))

multiplication_table_list = get_multiplication_table(user_table_size)

for row in multiplication_table_list:
    for symbol in row:
        print(f"{symbol: >{end_number}}", end=" ")
    print()
