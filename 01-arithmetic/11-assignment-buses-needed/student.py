# write your code here
from math import ceil
def buses_needed(people_count, bus_capacity):
    return ceil(people_count / bus_capacity)
print(buses_needed(7, 5))