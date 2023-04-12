def sieve(list_for_sort, heap_size, root_index):
    done = False

    while not done:
        max_index = root_index
        left_child_index = (2 * root_index) + 1
        right_child_index = (2 * root_index) + 2

        if left_child_index < heap_size and list_for_sort[left_child_index] > list_for_sort[max_index]:
            max_index = left_child_index

        if right_child_index < heap_size and list_for_sort[right_child_index] > list_for_sort[max_index]:
            max_index = right_child_index

        if max_index != root_index:
            list_for_sort[root_index], list_for_sort[max_index] = list_for_sort[max_index], list_for_sort[root_index]
            root_index = max_index
        else:
            done = True


def heap_sort(list_for_sort):
    list_length = len(list_for_sort)

    for i in range(list_length, -1, -1):
        sieve(list_for_sort, list_length, i)

    for i in range(list_length - 1, 0, -1):
        list_for_sort[i], list_for_sort[0] = list_for_sort[0], list_for_sort[i]
        sieve(list_for_sort, i, 0)


user_list_for_sort = [5, 9, 3, 4, 1, 6, 2, 8]

heap_sort(user_list_for_sort)

print(user_list_for_sort)
