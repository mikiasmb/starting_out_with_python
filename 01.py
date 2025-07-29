integer = int(input("Enter an integer: "))
eo = integer % 2
if integer > 0:
    print("Positive")
elif integer == 0:
    print("Zero")
else:
    print("Negative")
if eo == 0:
    print("Even")
else:
    print("Odd")
