day = int(input("Enter the number of days: "))
pennies = 0
total = 0
print("Day\t  Salary")
print("------------")
for i in range(0, day):
    pennies = 2 ** i
    total += pennies
    dollar = pennies / 100
    print(f"{i+1}\t\t${dollar:,.2f}", sep="")
print("total salary - $", f"{total / 100:,.2f}", sep="")
