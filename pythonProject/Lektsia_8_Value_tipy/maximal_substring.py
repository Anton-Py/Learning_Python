def search_maximal_substring(string):
    string = string.lower()
    max_substring = 1
    current_substring = 1

    if len(string) < 1:
        return "Строка пустая, введите верные данные"

    for i in range(0, len(string) - 1):
        if string[i] == string[i + 1]:
            current_substring += 1

            if current_substring > max_substring:
                max_substring = current_substring

        else:
            current_substring = 1

    return f"Максимальная длина подстроки равна: {max_substring}"


user_string = input("Введите строку: ")

print(search_maximal_substring(user_string))
