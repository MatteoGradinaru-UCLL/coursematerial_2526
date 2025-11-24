def valid_parentheses(string):
    balance_count = 0

    for char in string:
        if char == "(":
            balance_count += 1
        elif char == ")":
            balance_count -= 1
        if balance_count < 0:
            return False
        
    if balance_count != 0:
        return False
    
    return True