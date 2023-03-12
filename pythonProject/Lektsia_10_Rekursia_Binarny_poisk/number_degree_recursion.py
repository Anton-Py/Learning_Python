def get_number_degree(number, number_degree):
    if number_degree == 0:
        return 1
    return number * get_number_degree(number, number_degree - 1)


user_number = int(input("Введите число: "))
user_number_degree = int(input("Введите степень числа: "))

print(get_number_degree(user_number, user_number_degree))
