month = int(input("Enter a month (in numeric form): "))
day = int(input("Enter a day: "))
year = int(input("Enter a two digit year: "))
a = (month * day)
if a == year:
    print("The date is magic.")
else:
    print("The date is not magic.")
