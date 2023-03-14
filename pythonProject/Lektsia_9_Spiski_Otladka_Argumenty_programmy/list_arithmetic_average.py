def get_even_numbers_arithmetic_average(numbers_list):
    prime_numbers_sum = 0
    prime_numbers_quantity = 0

    for i in numbers_list:
        if i % 2 == 0:
            prime_numbers_sum += i
            prime_numbers_quantity += 1

    even_numbers_arithmetic_average = prime_numbers_sum / prime_numbers_quantity

    return even_numbers_arithmetic_average


entered_numbers_list = [int(i) for i in
                        input("Введите несколько числел через пробел, для создания списка: ").split()]

print("Среднее арифметическое элементов списка, которые являются четными числами:",
      get_even_numbers_arithmetic_average(entered_numbers_list))
