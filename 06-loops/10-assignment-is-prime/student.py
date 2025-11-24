def is_prime(n):

    if n == 1:
        return False

    for divisors in range(2, n):
        if n % divisors == 0:
            return False
    return True
        
print(is_prime(17))