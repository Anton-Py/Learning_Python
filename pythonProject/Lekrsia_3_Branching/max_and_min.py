num_one = int(input("Введите первое число: "))
num_two = int(input("Введите второе число: "))

# !
if num_one > num_two:
    print(f"Наибольшее число {num_one}, наименьшее число {num_two}")
else:
    print(f"Наибольшее число {num_two}, наименьшее число {num_one}")

# 2
maximum = num_one if num_one > num_two else num_two
minimum = num_one if num_one < num_two else num_two
print(f"Наибольшее число {maximum}, наименьшее число {minimum}")
