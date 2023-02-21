initial_number = int(input("Введите первоначальное число: "))
final_number = int(input("Введите конечное число: "))
col_num_in_string = int(input("Введите количество чисел в строке: "))

initial_number_iteration = 0
count_1 = 0
count_2 = 0

while initial_number_iteration < final_number:
    for f in range(initial_number, final_number + 1):
        count_1 += 1
        count_2 += 1
        initial_number_iteration = initial_number + count_1
        number_spaces = len(str(final_number)) - len(str(f))

        if number_spaces > 0:
            print(f"{' ' * number_spaces}{f}", end=" ")
        else:
            print(f"{f}", end=" ")

        if count_2 == col_num_in_string:
            print()
            count_2 = 0
