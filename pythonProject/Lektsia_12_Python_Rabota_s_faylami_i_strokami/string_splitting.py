def get_numbers_sum_in_string(list_to_splitting):
    numbers_list = list_to_splitting.split(",")
    numbers_sum = 0

    for i in numbers_list:
        numbers_sum += int(i)

    return numbers_sum


user_list_to_splitting = "5,9,3,4,1,6,2,8,10,3,16"

print(get_numbers_sum_in_string(user_list_to_splitting))
