def get_greatest_common_divisor(number_1, number_2):
    if number_1 == 0 and number_2 == 0:
        print("Наибольший общий делитель искать нельзя")
    elif number_2 == 0:
        greatest_common_divisor = number_1
    else:
        while number_2 != 0:
            number_1, number_2 = number_2, number_1 % number_2
    return number_1


user_number_1 = int(input("Введите первое число: "))
user_number_2 = int(input("Введите второе число: "))
print(f"Наибольший общий делитель = {get_greatest_common_divisor(user_number_1, user_number_2)}")
