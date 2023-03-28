def convert_file_to_uppercase():
    with open("data/input_data.txt", "r", newline="\r") as input_file, open("data/output.txt", "w") as output_file:
        for line in input_file.readlines():
            output_file.write(line.upper())


convert_file_to_uppercase()
