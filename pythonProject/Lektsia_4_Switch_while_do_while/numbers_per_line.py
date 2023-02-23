primary_number = int(input("Введите начальное число: "))
final_number = int(input("Введите конечное число: "))
quantity_numbers_per_line = int(input("Введите количество чисел в строке: "))

counter_to_count_in_line = 0

for f in range(primary_number, final_number + 1):
    counter_to_count_in_line += 1
    print(f"{f: >{len(str(final_number))}}", end=" ")

    if counter_to_count_in_line == quantity_numbers_per_line:
        print()
        counter_to_count_in_line = 0
