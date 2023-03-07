def check_palindrome(string):
    string = string.lower().replace(" ", "")
    string_length = len(string)

    if string[:string_length // 2] == string[string_length // 2 + 1:][::-1]:
        return "Cтрока является палиндромом"
    return "Cтрока не является палиндромом"


users_string = input("Введите строку: ")

print(check_palindrome(users_string))
