def product(a, b, c):

    if a is None and b is None and c is None:
        return 1
    elif a is None or b is None or c is None:
        if a is None:
            a = 1
        if b is None:
            b = 1
        if c is None:
            c = 1
    return a * b * c