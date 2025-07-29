years = int(input("Number of years: "))
months = 12
for i in range(years):
    total = 0
    average = 0
    for j in range(months):
        rainFall = float(input(f"Inches of rainfall for year{i + 1} month{j + 1}: "))
        total += rainFall
        average = total / months
    print(f"Total rainfall {total} inches")
    print(f"Average rainfall {average} inches")
