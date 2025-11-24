def is_digit(char):
    return "0" <= char <= "9"

def is_student_id(string):
    if len(string) != 8:
        return False
    
    first_char = string[0].lower()
    if first_char != "r" and first_char != "s":
        return False
    
    if not is_digit(string[1]):
        return False
    if not is_digit(string[2]):
        return False
    if not is_digit(string[3]):
        return False
    if not is_digit(string[4]):
        return False
    if not is_digit(string[5]):
        return False
    if not is_digit(string[6]):
        return False
    if not is_digit(string[7]):
        return False
    
    return True