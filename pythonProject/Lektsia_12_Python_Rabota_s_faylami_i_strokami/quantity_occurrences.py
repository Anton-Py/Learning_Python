def get_quantity_occurrences(text, string_to_search, start_index):
    string_with_text = text.lower()
    start = -1
    count = 0

    while True:
        start = string_with_text.find(string_to_search, start + start_index)

        if start == -1:
            break

        count += 1

    return count


def get_text_from_file():
    with open("data/input_data.txt", "r", newline="\r", encoding="utf-8") as input_file:
        return input_file.read()


text_from_file = get_text_from_file()
user_string_to_search = "файл"
user_start_index = 4

print("Число вхождений:", get_quantity_occurrences(text_from_file, user_string_to_search, user_start_index))
