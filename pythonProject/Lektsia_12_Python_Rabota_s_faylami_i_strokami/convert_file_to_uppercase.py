def convert_file_to_uppercase(input_file_path, output_path_file):
    with open(input_file_path, "r", encoding="utf-8") as input_file, \
            open(output_path_file, "w", encoding="utf-8") as output_file:
        for line in input_file:
            output_file.write(line.upper())


user_input_file_path = "data/input_data.txt"
user_output_path_file = "data/output.txt"

convert_file_to_uppercase(user_input_file_path, user_output_path_file)
