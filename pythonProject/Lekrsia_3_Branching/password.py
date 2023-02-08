password_user = str(input("Введите пароль: "))
password_constant = "movavi"

if password_constant == password_user:
    print("Пароль верный")
elif password_constant != password_user and len(password_user) > len(password_constant):
    print("Пароль неверный и строка слишком длинная")
elif password_constant != password_user and len(password_user) < len(password_constant):
    print("Пароль неверный и строка слишком короткая")
else:
    print("Пароль неверный")
