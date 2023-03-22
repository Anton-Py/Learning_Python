def convert_to_binary_tree(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        convert_to_binary_tree(nums, heap_size, largest)


def heap_sort(numbers_list):
    list_length = len(numbers_list)

    for i in range(list_length, -1, -1):
        convert_to_binary_tree(numbers_list, list_length, i)

    for i in range(list_length - 1, 0, -1):
        numbers_list[i], numbers_list[0] = numbers_list[0], numbers_list[i]
        convert_to_binary_tree(numbers_list, i, 0)

    return numbers_list


list_for_sort = [5, 9, 3, 4, 1, 6, 2, 8]

print(heap_sort(list_for_sort))
