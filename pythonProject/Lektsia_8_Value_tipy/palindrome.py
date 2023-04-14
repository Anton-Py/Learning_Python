def is_palindrome(string):
    if not string:
        return True

    i = 0
    j = len(string) - 1
    string = string.lower()

    while i <= j:
        if not string[i].isalpha():
            i += 1
            continue

        if not string[j].isalpha():
            j -= 1
            continue

        if string[i] != string[j]:
            return False

        j -= 1
        i += 1

    return True


user_string = input("Введите строку: ")

print("Является ли строка палиндромом:", is_palindrome(user_string))
