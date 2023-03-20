def insertion_sort(items):
    for i in range(1, len(items)):
        for j in range(i, 0, -1):
            if items[j] < items[j - 1]:
                tmp = items[j]
                items[j] = items[j - 1]
                items[j - 1] = tmp
            else:
                break

    return items


list_for_sort = [5, 9, 3, 4, 1, 6, 2, 8]

print(insertion_sort(list_for_sort))
