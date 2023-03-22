def get_number_in_power_with_recursion(number, exponent):
    if exponent == 0:
        return 1

    return number * get_number_in_power_with_recursion(number, exponent - 1)


def get_number_in_power(number, number_to_raise_in_power):
    numbers_product = 1

    for i in range(number_to_raise_in_power):
        numbers_product *= number

    return numbers_product


user_number = int(input("Введите число: "))
user_exponent = int(input("Введите степень числа: "))

print(f"Число {user_number} в степени {user_exponent} равно",
      get_number_in_power_with_recursion(user_number, user_exponent))
print(f"Число {user_number} в степени {user_exponent} равно",
      get_number_in_power(user_number, user_exponent))
