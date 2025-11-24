def group_by_first_letter(strings):
    result  = {}

    for string in strings:
        first_letter = string[0].upper()
        
        if first_letter not in result:
            result[first_letter] = []
        result[first_letter].append(string)

    return result


print(group_by_first_letter(['Anne', 'Albert', 'aardvark', 'Boris', 'Chris']))