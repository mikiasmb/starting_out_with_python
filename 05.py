mass = float(input("Enter mass of an object: "))
weight = mass * 9.8
print(f"{weight:,.2f} newton")
if weight > 500:
    print("Too heavy")
elif weight < 100:
    print("Too light")
