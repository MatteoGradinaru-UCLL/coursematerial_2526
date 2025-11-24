# write your code here
def last_character(string):
    if len(string) == 0:
        return None
    return string[-1]

print(last_character("hello_world"))