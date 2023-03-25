import random


def quick_sort(numbers_list, left, right):
    if left >= right:
        return

    random_list_element_on_segment = numbers_list[random.randint(left, right)]
    i = left
    j = right

    while i <= j:
        while numbers_list[i] < random_list_element_on_segment:
            i += 1

        while numbers_list[j] > random_list_element_on_segment:
            j -= 1

        if i <= j:
            temp = numbers_list[i]
            numbers_list[i] = numbers_list[j]
            numbers_list[j] = temp
            i += 1
            j -= 1

            quick_sort(numbers_list, left, j)
            quick_sort(numbers_list, i, right)


list_for_sort = [5, 9, 3, 4, 1, 6, 2, 8]

quick_sort(list_for_sort, 0, len(list_for_sort) - 1)
print(list_for_sort)
