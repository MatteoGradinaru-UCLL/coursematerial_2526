def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    skipped_tests = 0
    taken_tests = 0
    total_grade = 0
    
    if grade1 is None:
        skipped_tests += 1
    else:
        taken_tests += 1
        total_grade += grade1

    if grade2 is None:
        skipped_tests += 1 
    else:
        taken_tests += 1
        total_grade += grade2
    
    if grade3 is None:
        skipped_tests += 1
    else:
        taken_tests += 1
        total_grade += grade3
    
    if grade4 is None:
        skipped_tests += 1
    else:
        taken_tests += 1
        total_grade += grade4
    
    if grade5 is None:
        skipped_tests += 1
    else:
        taken_tests += 1
        total_grade += grade5

    if skipped_tests > 1:
        return False
    
    if (total_grade / taken_tests) >= 12:
        return True
    return False