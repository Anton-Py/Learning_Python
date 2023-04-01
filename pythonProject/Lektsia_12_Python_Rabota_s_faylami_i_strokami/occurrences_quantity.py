def get_occurrences_quantity(text, string_to_search):
    string_with_text = text.lower()
    string_search = string_to_search.lower()
    start_index = -1
    quantity = 0

    while True:
        start_index = string_with_text.find(string_search, start_index + 1)

        if start_index == -1:
            break

        quantity += 1

    return quantity


def get_text_from_file():
    with open("data/input_data.txt", "r", newline="\n", encoding="utf-8") as input_file:
        array = [row.strip() for row in input_file]
        return " ".join(array)


text_from_file = get_text_from_file()

user_string_to_search = "Файл"

print("Число вхождений:", get_occurrences_quantity(text_from_file, user_string_to_search))
