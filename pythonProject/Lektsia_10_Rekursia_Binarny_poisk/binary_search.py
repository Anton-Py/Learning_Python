def binary_search(list_for_search, value):
    if len(list_for_search) == 0:
        return -1

    left = 0
    right = len(list_for_search) - 1

    while left <= right:
        middle = (left + right) // 2

        if list_for_search[middle] == value:
            return middle

        if list_for_search[middle] < value:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def binary_search_with_recursion(list_for_search, value, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    if list_for_search[middle] == value:
        return middle
    elif list_for_search[middle] < value:
        return binary_search_with_recursion(list_for_search, value, middle + 1, right)
    else:
        return binary_search_with_recursion(list_for_search, value, left, middle - 1)


# user_list_for_search = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user_list_for_search = [2, 8, 5]
# user_list_for_search = []
user_value_for_search = 4

left_index = 0
right_index = len(user_list_for_search) - 1

print(binary_search(user_list_for_search, user_value_for_search))
print(binary_search_with_recursion(user_list_for_search, user_value_for_search, left_index, right_index))
