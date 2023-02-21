digits = int(input("Введите число: "))

sum_odd_digits = 0
max_digits = 0

a = digits // 1000
b = digits // 100 % 10
c = digits % 100 // 10
d = digits % 100 % 10

sum_digits = a + b + c + d

for f in (a, b, c, d):
    if f > max_digits:
        max_digits = f

    if f % 2 != 0:
        sum_odd_digits += f

print(f"Сумма цифр числа равна: {sum_digits}")
print(f"Сумма нечетных цифр числа равна: {sum_odd_digits}")
print(f"Максимальная цифра числа: {max_digits}")
