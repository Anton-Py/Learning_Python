def convert_file_to_uppercase(file_path, path_write):
    with open(file_path, "r", encoding="utf-8") as input_file, \
            open(path_write, "w", encoding="utf-8") as output_file:
        for line in input_file:
            output_file.write(line.upper())


input_file_path = "data/input_data.txt"
path_file_write = "data/output.txt"

convert_file_to_uppercase(input_file_path, path_file_write)
