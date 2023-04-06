def get_occurrences_quantity(text_from_file, search_string):
    quantity = 0
    start_index = 0
    text_from_file = text_from_file.lower()
    search_string = search_string.lower()

    while start_index < len(text_from_file):
        start_index = text_from_file.find(search_string, start_index)

        if start_index == -1:
            break

        quantity += 1
        start_index += 1

    return quantity


def get_text_from_file(path_read, string_to_search):
    quantity = 0

    with open(path_read, "r", encoding="utf-8") as input_file:
        while True:
            string = input_file.readline()
            quantity += get_occurrences_quantity(string, string_to_search)

            if not string:
                break

    return quantity


path_file_read = "data/input_data.txt"
user_search_string = "with"

print("Число вхождений:", get_text_from_file(path_file_read, user_search_string))
