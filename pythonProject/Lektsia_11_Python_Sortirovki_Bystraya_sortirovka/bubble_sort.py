def run_bubble_sort(items):
    for limit in range(len(items) - 1, -1, -1):
        swapped = False
        
        for i in range(limit):
            if items[i] > items[i + 1]:
                temp = items[i]
                items[i] = items[i + 1]
                items[i + 1] = temp
                swapped = True

        if not swapped:
            break

    return items


list_for_sort = [5, 9, 3, 4, 1, 6, 2, 8]

print(run_bubble_sort(list_for_sort))
