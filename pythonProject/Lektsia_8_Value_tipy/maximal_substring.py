def get_maximal_substring(string):
    string = string.lower()
    maximal_substring = 1
    temporal_substring = 1

    for i in range(0, len(string) - 1):
        if string[i] == string[i + 1]:
            temporal_substring += 1

            if temporal_substring > maximal_substring:
                maximal_substring = temporal_substring

        else:
            temporal_substring = 1
    return maximal_substring


users_string = input("Введите строку: ")

print(f"Максимальная длина подстроки равна: {get_maximal_substring(users_string)}")
