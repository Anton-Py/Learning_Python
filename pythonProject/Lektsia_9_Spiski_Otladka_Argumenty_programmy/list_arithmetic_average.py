def get_even_numbers_arithmetic_average(numbers_list):
    numbers_sum = 0
    numbers_quantity = 0

    for number in numbers_list:
        if number % 2 == 0:
            numbers_sum += number
            numbers_quantity += 1

    return numbers_sum / numbers_quantity


entered_numbers_list = [int(i) for i in
                        input("Введите несколько чисел через пробел, для создания списка: ").split()]

print("Среднее арифметическое элементов списка, которые являются четными числами:",
      get_even_numbers_arithmetic_average(entered_numbers_list))
