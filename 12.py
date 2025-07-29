sharesPurchased = 2000
stockPaid = 40
# two weeks later
sharesSold = 2000
stockSold = 42.75
# calculating
sp = (stockPaid * sharesPurchased)          # paid for the stock
commission1 = (sharesPurchased * stockPaid * .03)    # commission when he bought stocks
ss = (sharesSold * stockSold)                # sold the stock
commission2 = (stockSold * sharesSold * 0.03)        # commission when he sold stocks
moneyEarned = (sharesSold * stockSold)         # money received when he sold stocks
moneyLeft = (moneyEarned - commission2)       # money left when he paid his broker
profit = moneyEarned - moneyLeft
# displaying
print(f"The amount of money Joe paid for the stock is ${sp:,.2f}")
print(f"The amount of commission paid his broker after purchase is ${commission1:,.2f}")
print(f"The amount of money Joe sold the stock is ${ss:,.2f}")
print(f"The amount of commission Joe paid his broker after sold is ${commission2:,.2f}")
print(f"The amount of money Joe earned is ${moneyEarned:,.2f}")
print(f"The amount of money Joe left after he paid his broker is ${moneyLeft:,.2f}")
print(f"Joe's profit ${profit}")