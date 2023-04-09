def get_max_substring_length(string):
    if len(string) == 0:
        return 0

    string = string.lower()
    max_substring_length = 1
    current_substring_length = 1

    for i in range(0, len(string) - 1):
        if string[i] == string[i + 1]:
            current_substring_length += 1

            if current_substring_length > max_substring_length:
                max_substring_length = current_substring_length

        else:
            current_substring_length = 1

    return max_substring_length


user_string = input("Введите строку: ")

print("Длина максимальной подстроки:", get_max_substring_length(user_string))
