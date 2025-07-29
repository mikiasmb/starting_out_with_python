Tip = .18
Tax = 0.07
foodCharge = float(input("Enter the charge for the food: "))
# calculating
tip = foodCharge * Tip
tax = foodCharge * Tax
total = foodCharge + tip + tax
# displaying
print(f"Tip = ${tip:,.2f}")
print(f"Tax = ${tax:,.2f}")
print(f"Total = ${total:,.2f}")