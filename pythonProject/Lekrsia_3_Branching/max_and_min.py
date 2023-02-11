number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))

# !
if number_1 > number_2:
    print(f"Наибольшее число {number_1}, наименьшее число {number_2}")
else:
    print(f"Наибольшее число {number_2}, наименьшее число {number_1}")

# 2
maximum = number_1 if number_1 > number_2 else number_2
minimum = number_1 if number_1 < number_2 else number_2
print(f"Наибольшее число {maximum}, наименьшее число {minimum}")
