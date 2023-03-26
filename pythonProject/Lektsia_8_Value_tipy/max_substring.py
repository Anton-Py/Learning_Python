def get_max_substring_length(string):
    if len(string) == 0:
        return 0

    string = string.lower()
    max_length_for_substring = 1
    current_length_for_substring = 1

    for i in range(0, len(string) - 1):
        if string[i] == string[i + 1]:
            current_length_for_substring += 1

            if current_length_for_substring > max_length_for_substring:
                max_length_for_substring = current_length_for_substring

        else:
            current_length_for_substring = 1

    return max_length_for_substring


user_string = input("Введите строку: ")

print("Длина максимальной подстроки:", get_max_substring_length(user_string))
