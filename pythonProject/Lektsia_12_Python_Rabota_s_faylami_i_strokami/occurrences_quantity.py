def get_occurrences_quantity(text, string_to_search, start_index):
    string_with_text = text.lower()
    start = -1
    quantity = 0

    while True:
        start = string_with_text.find(string_to_search, start + start_index)

        if start == -1:
            break

        quantity += 1

    return quantity


def get_text_from_file():
    with open("data/input_data.txt", "r", newline="\r\n", encoding="utf-8") as input_file:
        return input_file.read()


text_from_file = get_text_from_file()
user_string_to_search = "файл"
user_start_index = 4

print("Число вхождений:", get_occurrences_quantity(text_from_file, user_string_to_search, user_start_index))
