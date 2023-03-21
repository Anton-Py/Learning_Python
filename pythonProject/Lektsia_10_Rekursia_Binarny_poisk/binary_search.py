def binary_search(list_for_search, value):
    left = 0
    right = len(list_for_search) - 1
    middle = (left + right) // 2

    if len(list_for_search) == 0:
        return -1

    while list_for_search[middle] != value and left <= right:
        if list_for_search[middle] < value:
            left = middle + 1
        else:
            right = middle - 1

        middle = (left + right) // 2

    if left > right:
        return -1

    return middle


def binary_search_with_recursion(list_for_search, value, left, right):
    if left > right:
        return -1
    else:
        middle = (left + right) // 2

        if list_for_search[middle] == value:
            return middle
        elif list_for_search[middle] < value:
            return binary_search_with_recursion(list_for_search, value, middle + 1, right)
        else:
            return binary_search_with_recursion(list_for_search, value, left, middle - 1)


# user_list_for_search = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# user_list_for_search = [8]
user_list_for_search = []
user_value_for_search = 8

left_index = 0
right_index = len(user_list_for_search) - 1

print(binary_search(user_list_for_search, user_value_for_search))
print(binary_search_with_recursion(user_list_for_search, user_value_for_search, left_index, right_index))
