first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

while first_number != 0 and second_number != 0:
    if first_number > second_number:
        first_number %= second_number
    else:
        second_number %= first_number

greatest_common_divisor = first_number + second_number

print(f"Наибольший общий делитель = {greatest_common_divisor}")
