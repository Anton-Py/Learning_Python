def quick_sort(list_for_sort, left, right):
    if left >= right:
        return

    support_member = list_for_sort[left]
    i = left
    j = right

    while i <= j:
        while list_for_sort[i] < support_member:
            i += 1

        while list_for_sort[j] > support_member:
            j -= 1

        if i <= j:
            temp = list_for_sort[i]
            list_for_sort[i] = list_for_sort[j]
            list_for_sort[j] = temp
            i += 1
            j -= 1

    quick_sort(list_for_sort, left, j)
    quick_sort(list_for_sort, i, right)


user_list_for_sort = [5, 9, 3, 4, 1, 6, 2, 8]

quick_sort(user_list_for_sort, 0, len(user_list_for_sort) - 1)
print(user_list_for_sort)
