# write your code here
def parse_day(string):
        return int(string[:2])
    

def parse_month(string):
        return int(string[3:5])
    

def parse_year(string):
    return int(string[6:10])


string = "01/02/2000"
print(parse_day(string))
print(parse_month(string))
print(parse_year(string))

