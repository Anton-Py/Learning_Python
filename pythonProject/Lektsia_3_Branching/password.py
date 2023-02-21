user_password = input("Введите пароль: ")

system_password = "movavi"

if system_password == user_password:
    print("Пароль верный")
elif len(user_password) > len(system_password):
    print("Пароль неверный и строка слишком длинная")
elif len(user_password) < len(system_password):
    print("Пароль неверный и строка слишком короткая")
else:
    print("Пароль неверный")
