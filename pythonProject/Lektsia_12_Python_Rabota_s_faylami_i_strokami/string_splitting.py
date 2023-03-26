def get_numbers_sum_in_string(string):
    string_list = string.split(", ")
    numbers_sum = 0
    numbers_list = []

    for i in string_list:
        number = int(i)
        numbers_sum += number
        numbers_list.append(number)

    print("Список из чисел строки:", numbers_list, "\n" "Cумма чисел строки:", numbers_sum)


user_string = "5, 9, 3, 4, 1, 6, 2, 8, 10, 3, 16"

get_numbers_sum_in_string(user_string)
