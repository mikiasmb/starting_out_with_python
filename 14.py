P = float(input("Enter the amount of principal originally deposited: "))
r = float(input("Enter the annual interest rate: ")) / 100
n = int(input("Enter the number of times per year that the interest is compounded: "))
t = int(input("Enter the number of years the account will earn interest: "))

A = P*(1+(r/n) ** n*t)
print(f"The amount of money in the account after {t} year is ${A}")
