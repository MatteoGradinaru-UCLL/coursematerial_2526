# write your code here
def all_different(xs):

    if len(xs) <= 1:
        return True
    
    for i in range(1, len(xs)):
        if 