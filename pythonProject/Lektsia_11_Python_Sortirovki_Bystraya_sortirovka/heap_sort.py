def sieve(list_to_sort, length_list):
    for i in range(length_list):

        if list_to_sort[i] > list_to_sort[int((i - 1) / 2)]:
            j = i

            while list_to_sort[j] > list_to_sort[int((j - 1) / 2)]:
                (list_to_sort[j], list_to_sort[int((j - 1) / 2)]) = (list_to_sort[int((j - 1) / 2)], list_to_sort[j])
                j = int((j - 1) / 2)


def heap_sort(list_to_sort, length_list):
    sieve(list_to_sort, length_list)

    for i in range(length_list - 1, 0, -1):

        list_to_sort[0], list_to_sort[i] = list_to_sort[i], list_to_sort[0]

        j = 0

        while True:
            index = 2 * j + 1

            if index < (i - 1) and list_to_sort[index] < list_to_sort[index + 1]:
                index += 1

            if index < i and list_to_sort[j] < list_to_sort[index]:
                list_to_sort[j], list_to_sort[index] = list_to_sort[index], list_to_sort[j]

            j = index

            if index >= i:
                break


user_list_to_sort = [10, 20, 15, 17, 9, 21]
length_the_list = len(user_list_to_sort)

heap_sort(user_list_to_sort, length_the_list)
print(user_list_to_sort)
