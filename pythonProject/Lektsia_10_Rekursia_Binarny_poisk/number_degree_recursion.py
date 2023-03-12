def get_number_degree_recursion(number, number_degree):
    if number_degree == 0:
        return 1

    return number * get_number_degree_recursion(number, number_degree - 1)


def get_number_degree(number, number_degree):
    numbers_product = 1
    for i in range(number_degree):
        numbers_product = numbers_product * number

    return numbers_product


def get_number_degree_through_cycle_while(number, number_degree):
    numbers_product = 1
    while number_degree != 0:
        numbers_product = numbers_product * number
        number_degree -= 1

    return numbers_product


user_number = int(input("Введите число: "))
user_number_degree = int(input("Введите степень числа: "))

print(get_number_degree_recursion(user_number, user_number_degree))
print(get_number_degree(user_number, user_number_degree))
print(get_number_degree_through_cycle_while(user_number, user_number_degree))
