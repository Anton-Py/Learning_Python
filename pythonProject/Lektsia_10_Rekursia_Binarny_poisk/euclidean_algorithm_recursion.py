def get_greatest_common_divisor(number_1, number_2):
    if number_2 == 0:
        return number_1

    return get_greatest_common_divisor(number_2, number_1 % number_2)


user_number_1 = int(input("Введите первое число: "))
user_number_2 = int(input("Введите второе число: "))

if user_number_1 == 0 and user_number_2 == 0:
    print("Наибольший общий делитель искать нельзя")
else:
    print(f"Наибольший общий делитель = {get_greatest_common_divisor(user_number_1, user_number_2)}")
