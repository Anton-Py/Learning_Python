import random


def generation_random_list_number():
    random_list = []
    for i in range(5):
        random_list.append(random.uniform(5, 20))
    print(random_list)
    return random_list


def search_maximum(list_numbers):
    epsilon = 0.0001
    maximal_number = epsilon

    for i in list_numbers:
        if i - maximal_number > epsilon:
            maximal_number = i

    return maximal_number


random_list_number = generation_random_list_number()

print("Максимальное число в списке вещественных чисел: ", search_maximum(random_list_number))
print("Максимальное число в списке вещественных чисел: ", max(random_list_number))
