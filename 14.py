weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

BMI = weight * 703 / (height ** height)
print(f"BMI = {BMI:,.2f}")

if 18.5 <= BMI <= 25:
    print("Your weight is optimal.")
elif BMI < 18.5:
    print("You are underweight.")
elif BMI > 25:
    print("You are overweight")
