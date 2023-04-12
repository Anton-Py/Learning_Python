def maxheap(arr, p):
    for i in range(len(arr) - p):
        if i > 0:
            child = i
            parent = (i + 1) // 2 - 1

            while arr[child] > arr[parent] and child != 0:
                arr[child], arr[parent] = arr[parent], arr[child]
                child = parent
                parent = (parent + 1) // 2 - 1


def heapsort(list_to_sort):
    for i in range(len(list_to_sort)):
        maxheap(list_to_sort, i)

        list_to_sort[0], list_to_sort[len(list_to_sort) - i - 1] = list_to_sort[len(list_to_sort) - i - 1], list_to_sort[0]

    return list_to_sort


user_list_to_sort = [10, 20, 15, 17, 9, 21]
length_the_list = len(user_list_to_sort)

print(heapsort(user_list_to_sort))
