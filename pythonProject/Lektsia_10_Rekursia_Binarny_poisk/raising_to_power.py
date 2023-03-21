def get_number_in_power_with_recursion(number, number_to_raise_in_power):
    if number_to_raise_in_power == 0:
        return 1

    return number * get_number_in_power_with_recursion(number, number_to_raise_in_power - 1)


def get_number_in_power(number, number_to_raise_in_power):
    numbers_product = 1

    for i in range(number_to_raise_in_power):
        numbers_product *= number

    return numbers_product


user_number = int(input("Введите число: "))
user_number_to_raise_in_power = int(input("Введите степень числа: "))

print(f"Число {user_number} в степени {user_number_to_raise_in_power} равно",
      get_number_in_power_with_recursion(user_number, user_number_to_raise_in_power))
print(f"Число {user_number} в степени {user_number_to_raise_in_power} равно",
      get_number_in_power(user_number, user_number_to_raise_in_power))
