def get_number_in_power_with_recursion(number, power):
    if power == 0:
        return 1

    return number * get_number_in_power_with_recursion(number, power - 1)


def get_number_in_power(number, power):
    numbers_product = 1

    for i in range(power):
        numbers_product *= number

    return numbers_product


user_number = int(input("Введите число: "))
user_power = int(input("Введите степень числа: "))

print(f"Число {user_number} в степени {user_power} равно",
      get_number_in_power_with_recursion(user_number, user_power))
print(f"Число {user_number} в степени {user_power} равно",
      get_number_in_power(user_number, user_power))
