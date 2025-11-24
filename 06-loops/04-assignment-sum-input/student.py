# write your code here
def sum_input():
    total = 0
    enter_it = int(input("Enter integer: "))

    while enter_it != 0:
        total += enter_it
        enter_it = int(input("Enter integer: "))
    
    print(f"The sum equals {total}.")

#print(sum_input())