def raising_to_power_with_recursion(number, number_degree):
    if number_degree == 0:
        return 1

    return number * raising_to_power_with_recursion(number, number_degree - 1)


def raising_to_power(number, number_degree):
    numbers_product = 1

    for i in range(number_degree):
        numbers_product *= number

    return numbers_product


user_number = int(input("Введите число: "))
user_number_degree = int(input("Введите степень числа: "))

print(raising_to_power_with_recursion(user_number, user_number_degree))
print(raising_to_power(user_number, user_number_degree))
