def selection_sort(list_for_sort):
    for i in range(len(list_for_sort) - 1):
        min_index = i

        for j in range(i + 1, len(list_for_sort)):
            if list_for_sort[min_index] > list_for_sort[j]:
                min_index = j

        temp = list_for_sort[i]
        list_for_sort[i] = list_for_sort[min_index]
        list_for_sort[min_index] = temp


user_list_for_sort = [5, 9, 3, 4, 1, 6, 2, 8]

selection_sort(user_list_for_sort)
print(user_list_for_sort)
