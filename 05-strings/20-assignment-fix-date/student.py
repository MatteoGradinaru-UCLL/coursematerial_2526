# write your code here
def fix_date(date):
    month = date[:2]
    day = date[3:5]
    year = date[6:10]

    return f"{year}/{month}/{day}"

print(fix_date("05/20/1999"))