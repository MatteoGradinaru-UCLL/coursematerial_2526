def remove_duplicates(xs):
    set_values = set()
    result = []

    for x in xs:
        if x not in set_values:
            set_values.add(x)
            result.append(x)
    return result


print(remove_duplicates([1, 3, 2, 2, 4, 1]))