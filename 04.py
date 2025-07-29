item1 = float(input("Enter the price of the 1st item: "))
item2 = float(input("Enter the price of the 2nd item: "))
item3 = float(input("Enter the price of the 3rd item: "))
item4 = float(input("Enter the price of the 4th item: "))
item5 = float(input("Enter the price of the 5th item: "))

Tax = 0.07
# calculating
Sub_total = item1 + item2 + item3 + item4 + item5
Sales_tax = Sub_total * Tax
Total = Sub_total + Sales_tax
# displaying
print(f"Sub_Total = ${Sub_total:,.2f}")
print(f"Sales_Tax = ${Sales_tax:,.2f}")
print(f"Total = ${Total:,.2f}")
