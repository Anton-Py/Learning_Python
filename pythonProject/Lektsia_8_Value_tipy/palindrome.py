# вариант №1
def is_check_palindrome(string):
    count = 1
    result = True

    for i in string.lower():

        if i == " ":
            continue
        elif string.lower()[-count] == " ":
            count += 1

            if i == string.lower()[-count]:
                result = True

        elif i == string.lower()[-count]:
            result = True
        else:
            result = False
        count += 1

    return result


# вариант №2
def is_check_palindrome_2(string):
    if string.lower() == string.lower()[::-1]:
        return True
    return False


users_string = input("Введите строку: ")

print(is_check_palindrome(users_string))
print(is_check_palindrome_2(users_string))
