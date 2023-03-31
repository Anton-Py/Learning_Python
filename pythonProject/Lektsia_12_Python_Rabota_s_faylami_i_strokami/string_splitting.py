def numbers_sum_in_string(string):
    strings_list = string.split(", ")
    numbers_sum = 0
    numbers_list = []

    for i in strings_list:
        number = int(i)
        numbers_sum += number
        numbers_list.append(number)

    return numbers_list, numbers_sum


user_string = "5, 9, 3, 4, 1, 6, 2, 8, 10, 3, 16"

data = numbers_sum_in_string(user_string)

print("Список из чисел строки:", data[0], "\n" "Сумма чисел строки:", data[1])
