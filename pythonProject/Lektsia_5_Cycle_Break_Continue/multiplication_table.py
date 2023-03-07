end_number = int(input("Введите конечное число: "))

end_number_square_length = len(str(end_number ** 2))
end_number_length = len(str(end_number))

# отступ в шапке для цифр
if end_number_square_length < 2:
    print(end=" " * (end_number_square_length + 3))
else:
    print(end=" " * (end_number_square_length + 2))

# выводим шапку
for i in range(1, end_number + 1):
    print(f"{i: >{end_number_square_length}}|", end=" ")

print()

# отступ в шапке для разделителя
if end_number_square_length < 2:
    print(end=" " * (end_number_square_length + 2))
else:
    print(end=" " * (end_number_square_length + 1))

# выводим разделитель
for i in range(1, end_number + 1):
    print(f"{'--': >{end_number_square_length + 1}}", end=" ")

print()

# выводим таблицу умножения
for i in range(1, end_number + 1):
    print(f"{i: >{end_number_length}}|", end=" ")

    for j in range(1, end_number + 1):
        numbers_product = i * j
        print(f"{numbers_product: >{end_number_square_length + 1}}", end=" ")

    print()
