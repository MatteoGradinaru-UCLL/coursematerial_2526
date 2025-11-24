# write your code here
def box(string):
    length = (len(string) + 2) * "-"
    border = "+"
    return f"{border}{length}{border}\n| {string} |\n{border}{length}{border}"


print(box("Put me in the box"))