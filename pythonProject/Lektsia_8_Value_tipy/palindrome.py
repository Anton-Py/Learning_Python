def is_palindrome(string):
    count = 1
    string = string.lower()

    while True:
        for i in range(len(string)):
            if not string[i].isalpha():
                continue

            if not string[-count].isalpha():
                count += 1

            elif string[i] != string[-count]:
                return False

            count += 1

        return True


users_string = input("Введите строку: ")

print(is_palindrome(users_string))
