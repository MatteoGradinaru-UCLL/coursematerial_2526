def multiple_choice(right_answer, given_answer):
    points = 0

    if given_answer == right_answer:
        points += 1
    elif given_answer is None:
        points += 0
    else:
        points -= 0.2
    
    return points