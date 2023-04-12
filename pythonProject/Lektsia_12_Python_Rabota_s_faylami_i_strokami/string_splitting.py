def get_numbers_list_and_numbers_sum_in_string(string_data):
    strings_list = string_data.split(", ")
    numbers_sum = 0
    numbers_list = []

    for string in strings_list:
        number = int(string)
        numbers_sum += number
        numbers_list.append(number)

    return numbers_list, numbers_sum


entered_user_string = "5, 9, 3, 4, 1, 6, 2, 8, 10, 3, 16"

data = get_numbers_list_and_numbers_sum_in_string(entered_user_string)

print("Список из чисел строки:", data[0], "\n" "Сумма чисел строки:", data[1])
