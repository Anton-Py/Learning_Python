def is_palindrome(string):
    j = -1
    i = 0
    string = string.lower()

    while i < len(string) // 2:
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
