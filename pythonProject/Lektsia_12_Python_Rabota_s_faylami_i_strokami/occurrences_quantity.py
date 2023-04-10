def get_occurrences_quantity(text, search_string):
    text = text.lower()
    search_string = search_string.lower()
    start_index = 0
    quantity = 0

    index = text.find(search_string, start_index)

    while index != -1:
        start_index = index + 1
        quantity += 1

        index = text.find(search_string, start_index)

    return quantity


def get_total_occurrences_quantity(input_file_path, string_to_search):
    quantity = 0

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        while True:
            line = input_file.readline()
            quantity += get_occurrences_quantity(line, string_to_search)

            if not line:
                break

    return quantity


user_input_file_path = "data/input_data.txt"
user_search_string = "файл"

print("Число вхождений:", get_total_occurrences_quantity(user_input_file_path, user_search_string))
