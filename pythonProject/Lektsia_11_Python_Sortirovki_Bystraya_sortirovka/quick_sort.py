# 1

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    elif len(lst) == 2:
        if lst[0] > lst[1]:
            temp = lst[0]
            lst[0] = lst[1]
            lst[1] = temp
    else:
        support_element = lst[0]
        left_elements = list(i for i in lst if i < support_element)
        central_element = list(i for i in lst if i == support_element)
        right_elements = list(i for i in lst if i > support_element)

        lst = quick_sort(left_elements) + central_element + quick_sort(right_elements)

    return lst


# 2

def quick_sort_2(lst, left, right):
    if left >= right:
        return
    else:
        q = lst[0]
        i = left
        j = right
        while i <= j:
            while lst[i] < q:
                i += 1
            while lst[j] > q:
                j -= 1
            if i <= j:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
                i += 1
                j -= 1
                quick_sort_2(lst, left, j)
                quick_sort_2(lst, i, right)

    return lst


list_for_sort = [5, 9, 3, 4, 1, 6, 2, 8]

print(quick_sort(list_for_sort))
print(quick_sort_2(list_for_sort, 0, len(list_for_sort) - 1))
