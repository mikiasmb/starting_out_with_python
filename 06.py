purchase = float(input("Enter the amount of purchase: "))
instalments = float(input("Enter the desired number of payment instalments: "))
# calculating
totalPurchase = purchase * .05
eachInstalment = totalPurchase / instalments
# displaying
print(f"Total amount of the purchase is ${totalPurchase:,.2f}")
print(f"Each instalment will cost ${eachInstalment:,.2f}")