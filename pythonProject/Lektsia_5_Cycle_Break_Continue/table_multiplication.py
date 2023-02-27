end_number = int(input("Введите конечное число: "))

length_end_number_square = len(str(end_number ** 2))
length_end_number = len(str(end_number))

# отступ в шапке для цифр
print(end=" " * (length_end_number_square + 1))
# выводим шапку
for i in range(1, end_number + 1):
    print(f"{i: >{length_end_number_square - 1}}|", end=" ")
print()
# отступ в шапке для разделителя
print(end=" " * (length_end_number_square + 1))
# выводим разделитель
for i in range(1, end_number + 1):
    print(f"{'--': >{length_end_number_square}}", end=" ")
print()
# выводим таблицу умножения
for i in range(1, end_number + 1):
    print(f"{i: >{length_end_number}}|", end=" ")
    for j in range(1, end_number + 1):
        c = i * j
        print(f"{c: >{length_end_number_square}}", end=" ")
    print()
