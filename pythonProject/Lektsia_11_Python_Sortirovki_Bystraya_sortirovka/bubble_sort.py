def is_bubble_sort(items):
    for limit in range(len(items) - 1, 0, -1):
        swapped = False

        for i in range(limit):
            if items[i] > items[i + 1]:
                temp = items[i]
                items[i] = items[i + 1]
                items[i + 1] = temp

                swapped = True

        if not swapped:
            break


list_for_sort = [5, 9, 3, 4, 1, 6, 2, 8, 10, 3, 16]

is_bubble_sort(list_for_sort)
