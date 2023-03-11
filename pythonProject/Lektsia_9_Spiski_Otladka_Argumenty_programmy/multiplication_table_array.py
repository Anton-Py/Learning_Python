def fill_in_multiplication_table(table_size):
    array = []

    for i in range(table_size):
        nested_array = [i for i in range(table_size)]
        array.append(nested_array)

    for i in range(table_size):
        for j in range(table_size):
            array[i][j] = i * j

    for i in array:
        print(i)


user_table_size = int(input("Введите число, которое задает размер таблицы: "))

fill_in_multiplication_table(user_table_size)
