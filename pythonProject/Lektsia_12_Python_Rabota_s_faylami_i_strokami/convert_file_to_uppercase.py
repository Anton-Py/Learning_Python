def convert_file_to_uppercase(path_read, path_write):
    with open(path_read, "r", encoding="utf-8") as input_file, \
            open(path_write, "w", newline="\n", encoding="utf-8") as output_file:
        for line in input_file:
            if line.strip():
                output_file.write(line.upper())


path_file_read = "data/input_data.txt"
path_file_write = "data/output.txt"

convert_file_to_uppercase(path_file_read, path_file_write)
