number = int(input("Введите число: "))

digits_odd_sum = 0
digit_sum = 0
max_digit = 0

while number > 0:
    digit = number % 10
    digit_sum += digit

    if digit > max_digit:
        max_digit = digit

    if digit % 2 != 0:
        digits_odd_sum += digit
    number = number // 10

print(f"Сумма цифр числа равна: {digit_sum}")
print(f"Сумма нечетных цифр числа равна: {digits_odd_sum}")
print(f"Максимальная цифра числа: {max_digit}")
