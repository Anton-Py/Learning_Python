def fill_in_multiplication_table(table_size):
    list_for_multiplication = []

    for i in range(1, table_size + 1):
        nested_array = [i for i in range(1, table_size + 1)]
        list_for_multiplication.append(nested_array)

    for i in range(table_size):
        for j in range(table_size):
            list_for_multiplication[i][j] = (i + 1) * (j + 1)

    return list_for_multiplication


user_table_size = int(input("Введите число, которое задает размер таблицы: "))

multiplication_table = fill_in_multiplication_table(user_table_size)

for j in multiplication_table:
    print(j)
