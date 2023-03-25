# 1

def quick_sort(numbers_list):
    if len(numbers_list) <= 1:
        return numbers_list
    elif len(numbers_list) == 2:
        if numbers_list[0] > numbers_list[1]:
            temp = numbers_list[0]
            numbers_list[0] = numbers_list[1]
            numbers_list[1] = temp
    else:
        support_element = numbers_list[0]
        left_elements = list(i for i in numbers_list if i < support_element)
        central_element = list(i for i in numbers_list if i == support_element)
        right_elements = list(i for i in numbers_list if i > support_element)

        numbers_list = quick_sort(left_elements) + central_element + quick_sort(right_elements)

    return numbers_list


# 2

def quick_sort_2(numbers_list, left, right):
    if left >= right:
        return
    else:
        q = numbers_list[0]
        i = left
        j = right
        while i <= j:
            while numbers_list[i] < q:
                i += 1
            while numbers_list[j] > q:
                j -= 1
            if i <= j:
                temp = numbers_list[i]
                numbers_list[i] = numbers_list[j]
                numbers_list[j] = temp
                i += 1
                j -= 1
                quick_sort_2(numbers_list, left, j)
                quick_sort_2(numbers_list, i, right)

    return numbers_list


list_for_sort = [5, 9, 3, 4, 1, 6, 2, 8]

print(quick_sort(list_for_sort))
print(quick_sort_2(list_for_sort, 0, len(list_for_sort) - 1))
