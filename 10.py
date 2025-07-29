sugar = 1.5
butter = 1
flour = 2.75
tCookies = 48
cookies = int(input("How many cookies do you want to make: "))
# calculating needed amount
nSugar = format((sugar * cookies) / tCookies, ',.2f')
nButter = format((butter * cookies) / tCookies, ',.2f')
nFlour = format((flour * cookies) / tCookies, ',.2f')
#displaying
print(f"You need {nSugar} cup of sugar.")
print(f"You need {nButter} cup of butter.")
print(f"You need {nFlour} cup of flour.")