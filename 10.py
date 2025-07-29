pennies = int(input("Enter the number of pennies: "))
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarters: "))

total_value = (pennies * .01) + (nickels * .05) + (dimes * .1) + (quarters * .25)

if total_value == 1.0:
    print("Congratulations! You've won.")
elif total_value < 1.0:
    print(f"Sorry, the total value is less than one dollar. You entered ${total_value:.2f}.")
else:
    print(f"Sorry, the total value is more than one dollar. You entered ${total_value:.2f}.")
