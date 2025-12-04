def remove_empty_lines(source, destination):

    with open(source, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

    with open(destination, "w", encoding="utf-8") as output_file:
        for line in lines:
            if line != "\n":
                output_file.write(line)