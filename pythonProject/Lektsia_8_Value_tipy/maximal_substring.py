def get_max_substring_length(string):
    if len(string) == 0:
        return 0

    string = string.lower()
    max_value = 1
    current_value = 1

    for i in range(0, len(string) - 1):
        if string[i] == string[i + 1]:
            current_value += 1

            if current_value > max_value:
                max_value = current_value

        else:
            current_value = 1

    return max_value


user_string = input("Введите строку: ")

print("Длина максимальной подстроки:", get_max_substring_length(user_string))
