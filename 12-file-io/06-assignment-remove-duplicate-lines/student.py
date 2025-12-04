def remove_duplicate_lines(source, destination):

    with open(source, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()



    with open(destination, "w", encoding="utf-8") as output_file:
        if not lines:
            return

        output_file.write(lines[0])


        for char in range(1, len(lines)):
            if lines[char] != lines[char-1]:
                output_file.write(lines[char])
