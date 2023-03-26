def sieve(nums, heap_size, root_index):
    max_index = root_index
    left_child_index = (2 * root_index) + 1
    right_child_index = (2 * root_index) + 2

    if left_child_index < heap_size and nums[left_child_index] > nums[max_index]:
        max_index = left_child_index

    if right_child_index < heap_size and nums[right_child_index] > nums[max_index]:
        max_index = right_child_index

    if max_index != root_index:
        nums[root_index], nums[max_index] = nums[max_index], nums[root_index]
        sieve(nums, heap_size, max_index)


def heap_sort(numbers_list):
    list_length = len(numbers_list)

    for i in range(list_length, -1, -1):
        sieve(numbers_list, list_length, i)

    for i in range(list_length - 1, 0, -1):
        numbers_list[i], numbers_list[0] = numbers_list[0], numbers_list[i]
        sieve(numbers_list, i, 0)

    return numbers_list


list_for_sort = [5, 9, 3, 4, 1, 6, 2, 8]

print(heap_sort(list_for_sort))
