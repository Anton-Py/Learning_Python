def get_occurrences_quantity(text, string):
    text = text.lower()
    string = string.lower()
    start_index = 0
    quantity = 0

    index = text.find(string, start_index)

    while index != -1:
        start_index = index + len(string)
        quantity += 1

        index = text.find(string, start_index)

    return quantity


def get_total_occurrences_quantity(input_file_path, search_string):
    quantity = 0

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        for line in input_file:
            quantity += get_occurrences_quantity(line, search_string)

    return quantity


user_input_file_path = "data/input_data.txt"
user_search_string = "можно"

print("Число вхождений:", get_total_occurrences_quantity(user_input_file_path, user_search_string))

