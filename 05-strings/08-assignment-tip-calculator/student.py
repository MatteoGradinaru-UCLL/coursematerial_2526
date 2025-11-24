# # write your code here
def tip_calculator():
    total_price = float(input("Enter total price: "))
    tip_percentage = input("Enter tip percentage (default=20): ")

    if tip_percentage == "":
        tip_percentage = 20
    else:
        tip_percentage = int(tip_percentage)

    total_amount = round((total_price * tip_percentage / 100) + total_price)
    print(f"You have to pay {total_amount}")