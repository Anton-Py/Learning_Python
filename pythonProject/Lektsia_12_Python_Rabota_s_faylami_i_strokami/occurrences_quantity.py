def get_occurrences_quantity(text, string_search):
    text = text.lower()
    string_search = string_search.lower()
    start_index = 0
    quantity = 0

    index = text.find(string_search, start_index)

    while index != -1:
        start_index = index + 1
        quantity += 1

        index = text.find(string_search, start_index)

    return quantity


def get_total_occurrences_quantity(input_file_path, string_to_search):
    quantity = 0

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        for line in input_file:
            quantity += get_occurrences_quantity(line, string_to_search)

    return quantity


user_input_file_path = "data/input_data.txt"
user_string_to_search = "with"

print("Число вхождений:", get_total_occurrences_quantity(user_input_file_path, user_string_to_search))

