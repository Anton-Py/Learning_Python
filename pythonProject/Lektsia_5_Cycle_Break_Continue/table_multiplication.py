final_number = int(input("Введите конечное число: "))

# отступ в шапке для цифр
print(end=" " * (len(str(final_number ** 2)) + 1))
# выводим шапку
for i in range(1, final_number + 1):
    print(f"{i: >{(len(str(final_number ** 2))) - 1}}|", end=" ")
print()
# отступ в шапке для разделителя
print(end=" " * (len(str(final_number ** 2)) + 1))
# выводим разделитель
for i in range(1, final_number + 1):
    print(f"{'--': >{len(str(final_number ** 2))}}", end=" ")
print()
# выводим таблицу умножения
for i in range(1, final_number + 1):
    print(f"{i: >{len(str(final_number))}}|", end=" ")
    for j in range(1, final_number + 1):
        c = i * j
        print(f"{c: >{len(str(final_number ** 2))}}", end=" ")
    print()
