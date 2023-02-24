fixed_string = "abcd"

while True:
    user_string = input("Введите строку: ")

    if user_string == fixed_string:
        print("Вы ввели верную строку")
        break
    else:
        print("Вы ввели не верную строку")
