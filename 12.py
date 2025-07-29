num_purchased = int(input("Enter the number of packages purchased: "))

retails = 99
discount = 0
price = retails * num_purchased

if 10 <= num_purchased <= 19:
    discount = .1
elif 20 <= num_purchased <= 49:
    discount = .2
elif 50 <= num_purchased <= 99:
    discount = .3
elif 100 <= num_purchased:
    discount = .4

dis_price = price * discount            # price after discount
print(f"Amount of discount = {discount:.0%}")
print(f"Total amount of purchase = ${dis_price:,.2f}")
