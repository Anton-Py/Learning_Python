def insertion_sort(items):
    for i in range(1, len(items)):
        temp = items[i]
        j = i - 1

        while j >= 0 and temp < items[j]:
            items[j + 1] = items[j]
            j -= 1

        items[j + 1] = temp


list_for_sort = [5, 9, 3, 4, 1, 6, 2, 8]

insertion_sort(list_for_sort)
print(list_for_sort)
