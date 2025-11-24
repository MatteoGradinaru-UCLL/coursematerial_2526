# write your code here
def is_valid_month(month):
    return 1 <= month <= 12

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def has_30_days(month):
    return month % 30 == 0 