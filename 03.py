month = int(input("Enter a month as a number b/n 1 & 12: "))

if 1 <= month <= 3:
    print("Month is in first quarter")
elif 4 <= month <= 6:
    print("Month is in second quarter")
elif 7 <= month <= 9:
    print("Month is in third quarter")
elif 10 <= month <= 12:
    print("Month is in fourth quarter")
else:
    print("error")
