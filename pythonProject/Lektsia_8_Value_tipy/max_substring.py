def get_max_substring_length(string):
    if len(string) == 0:
        return 0

    string = string.lower()
    substring_of_max_length = 1
    substring_of_current_length = 1

    for i in range(0, len(string) - 1):
        if string[i] == string[i + 1]:
            substring_of_current_length += 1

            if substring_of_current_length > substring_of_max_length:
                substring_of_max_length = substring_of_current_length

        else:
            substring_of_current_length = 1

    return substring_of_max_length


user_string = input("Введите строку: ")

print("Длина максимальной подстроки:", get_max_substring_length(user_string))
