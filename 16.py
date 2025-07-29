year = int(input("Enter a year: "))
leap1 = year % 100
leap2 = year % 400
leap3 = year % 4

if (leap1 == 0) and (leap2 == 0):
    print(f"In {year} February has 29 days.")
elif (leap1 != 0) and (leap3 == 0):
    print(f"In {year} February has 29 days.")
else:
    print(f"In {year} February has 28 days.")
