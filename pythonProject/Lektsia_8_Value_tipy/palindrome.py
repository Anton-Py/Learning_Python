def is_palindrome(string):
    if not string:
        return True

    i = 0
    j = len(string) - 1
    symbol_isalpha = False
    string = string.lower()

    while i <= j:
        if not string[i].isalpha():
            i += 1
            continue
        else:
            symbol_isalpha = True

        if not string[j].isalpha():
            j -= 1
            continue

        if string[i] != string[j]:
            return False

        j -= 1
        i += 1

    if not symbol_isalpha:
        return False

    return True


user_string = input("Введите строку: ")

print("Является ли строка палиндромом:", is_palindrome(user_string))
