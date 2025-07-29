weight = float(input("Enter the weight of a package: "))
price = 0

if weight <= 2:
    price = 1.5
elif 2 < weight <= 6:
    price = 3
elif 6 < weight <= 10:
    price = 4
elif weight > 10:
    price = 4.75

charge = weight * price
print(f"The ship ping charges ${charge:,.2f}")
