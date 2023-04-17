def sieve(list_for_sort, heap_size, root_index):
    while True:
        max_index = root_index
        left_child_index = (2 * root_index) + 1
        right_child_index = (2 * root_index) + 2

        if left_child_index < heap_size and list_for_sort[left_child_index] > list_for_sort[max_index]:
            max_index = left_child_index

        if right_child_index < heap_size and list_for_sort[right_child_index] > list_for_sort[max_index]:
            max_index = right_child_index

        if max_index == root_index:
            return

        list_for_sort[root_index], list_for_sort[max_index] = list_for_sort[max_index], list_for_sort[root_index]
        root_index = max_index


def heap_sort(list_for_sort):
    list_length = len(list_for_sort)

    for i in range((list_length // 2) - 1, -1, -1):
        sieve(list_for_sort, list_length, i)

    for i in range(list_length - 1, 0, -1):
        list_for_sort[i], list_for_sort[0] = list_for_sort[0], list_for_sort[i]
        sieve(list_for_sort, i, 0)


user_list_for_sort = [15, 5, 11, 9, 12, 10, 3, 16, 4, 14, 1, 6, 2, 18, 8, 13]

heap_sort(user_list_for_sort)

print(user_list_for_sort)
