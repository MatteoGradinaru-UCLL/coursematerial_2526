# write your code here
import random
def generate_number(n):
    return round(1 + random.random() * (n - 1), 1)

def fake_casino_revisited(n):
    random.seed(42)

    print(generate_number(n))
    print(generate_number(n))
    print(generate_number(n))
    print(generate_number(n))
    print(generate_number(n))