def get_max_number(numbers_list):
    max_number = numbers_list[0]

    for number in numbers_list:
        if number > max_number:
            max_number = number

    return max_number


random_numbers_list = [float(i) for i in input(
    "Введите несколько вещественных чисел через пробел, для создания списка: ").split()]

print("Максимальное число в списке вещественных чисел:", get_max_number(random_numbers_list))
print("Максимальное число в списке вещественных чисел:", max(random_numbers_list))
