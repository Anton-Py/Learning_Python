def get_arithmetic_average_even_numbers(list_to_arithmetic_average):
    prime_numbers_sum = 0
    prime_numbers_quantity = 0

    for i in list_to_arithmetic_average:
        if int(i) % 2 == 0:
            prime_numbers_sum += int(i)
            prime_numbers_quantity += 1

    arithmetic_average_even_numbers = prime_numbers_sum / prime_numbers_quantity

    return arithmetic_average_even_numbers


entered_list_to_arithmetic_average = input("Введите несколько числел через пробел, для создания списка: ").split()

print("Среднее арифметическое элементов списка, которые являются четными числами:",
      get_arithmetic_average_even_numbers(entered_list_to_arithmetic_average))
