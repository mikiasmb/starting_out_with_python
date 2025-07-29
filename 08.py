total = 0
while True:
    number = float(input("Enter a number: "))
    if number < 0:
        break
    total += number
print(f"Total sum - {total:,.2f}")
