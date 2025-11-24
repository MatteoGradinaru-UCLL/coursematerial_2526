# def gcd(x, y):
#     count = 0

#     if x[0] == "-" or y[0] == "-":
#         x = x[1:]
#         y = y[1:]
    
    
#     greatest_num = None
#     if x >= y:
#         x == greatest_num
#     else:
#         y == greatest_num

#     for divisor in range(greatest_num, 1, -1):
#         if x % divisor == 0 and y % divisor == 0:
#             return divisor


def gcd(x, y):
    return max([d for d in range(1 , max([abs(x), abs(y)]) + 1) if x % d == 0 and y % d == 0])
    

print(gcd(5, 7))
print(gcd(15, 10))
print(gcd(10, -15))