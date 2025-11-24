def find_duplicates(xs):
    duplicates = set()
    seen = set()

    for item in xs:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)