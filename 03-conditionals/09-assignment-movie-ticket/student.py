# write your code here
from math import ceil

def movie_ticket(duration, imax, student, ticket_count):
    tot_price = 0

    if duration <= 90:
        tot_price += 10
    elif duration <= 120:
        tot_price += 11
    elif duration <= 150:
        tot_price += 12
    else:
        tot_price += 15

    if imax:
        tot_price += ceil(tot_price * 0.2)

    if student:
        tot_price -= 3

    return tot_price * ticket_count

print(movie_ticket(180, True, False, 1))