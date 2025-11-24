# write your code here
def split_name(full_name):
    for char in full_name:
        if char == " ":
            first_name, last_name = full_name.split(" ")
            return first_name, last_name
    return full_name


print(split_name("John Doe"))