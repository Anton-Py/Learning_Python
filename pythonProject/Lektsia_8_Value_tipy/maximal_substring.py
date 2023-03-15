def get_maximal_length_substring(string):
    if len(string) == 0:
        return 0

    string = string.lower()
    temp_substring = 1
    temp_current_substring = 1

    for i in range(0, len(string) - 1):
        if string[i] == string[i + 1]:
            temp_current_substring += 1

            if temp_current_substring > temp_substring:
                temp_substring = temp_current_substring

        else:
            temp_current_substring = 1

    return temp_substring


user_string = input("Введите строку: ")

print(get_maximal_length_substring(user_string))
