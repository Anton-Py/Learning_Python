def bubble_sort(items):
    for limit in range(len(items) - 1, 0, -1):
        is_swapped = False

        for i in range(limit):
            if items[i] > items[i + 1]:
                temp = items[i]
                items[i] = items[i + 1]
                items[i + 1] = temp

                is_swapped = True

        if not is_swapped:
            return


list_for_sort = [5, 9, 3, 4, 1, 6, 2, 8, 10, 3, 16]

bubble_sort(list_for_sort)
print(list_for_sort)
