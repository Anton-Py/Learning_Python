def run_selection_sort(numbers_list):
    for i in range(len(numbers_list)):
        min_index = i

        for j in range(i + 1, len(numbers_list)):
            if numbers_list[min_index] > numbers_list[j]:
                min_index = j

        tmp = numbers_list[i]
        numbers_list[i] = numbers_list[min_index]
        numbers_list[min_index] = tmp

    return numbers_list


list_for_sort = [5, 9, 3, 4, 1, 6, 2, 8]

print(run_selection_sort(list_for_sort))
