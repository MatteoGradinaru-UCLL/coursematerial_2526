# write your code here
def thanos(queue_size, target_size):
    counter = 0
    i = queue_size
    while i > target_size:
        i = i / 2
        counter += 1
    return counter

print(thanos(100, 10))