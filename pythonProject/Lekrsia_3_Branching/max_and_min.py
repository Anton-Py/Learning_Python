num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

# !
if num_1 > num_2:
    print(f"Наибольшее число {num_1}, наименьшее число {num_2}")
else:
    print(f"Наибольшее число {num_2}, наименьшее число {num_1}")

# 2
maximum = num_1 if num_1 > num_2 else num_2
minimum = num_1 if num_1 < num_2 else num_2
print(f"Наибольшее число {maximum}, наименьшее число {minimum}")
