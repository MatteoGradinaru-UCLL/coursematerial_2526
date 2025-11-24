# write your code here
def all_equal(xs):
    
    if len(xs) <= 1:
        return True
    
    for i in range(1, len(xs)):
        if xs[i] != xs[0]:
            return False
    return True

#print(all_equal((1, 1, 1)))