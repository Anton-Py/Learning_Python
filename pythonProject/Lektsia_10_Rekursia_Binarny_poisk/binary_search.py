def binary_search(lst, value):
    left = 0
    right = len(lst) - 1
    middle = (left + right) // 2

    while lst[middle] != value and left <= right:

        if lst[middle] < value:
            left = middle + 1
        else:
            right = middle - 1

        middle = (left + right) // 2

    if left > right:
        return -1
    else:
        return middle


def binary_search_with_recursion(lst, value, left, right):
    if left > right:
        return -1
    else:
        middle = (left + right) // 2

        if lst[middle] == value:
            return middle
        elif lst[middle] < value:
            return binary_search_with_recursion(lst, value, middle + 1, right)
        else:
            return binary_search_with_recursion(lst, value, left, middle - 1)


list_for_search = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
value_for_search = 11

left_index = 0
right_index = len(list_for_search) - 1

print(binary_search(list_for_search, value_for_search))
print(binary_search_with_recursion(list_for_search, value_for_search, left_index, right_index))
