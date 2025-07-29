rainFalls = []
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

print("Enter the total rainfall of each month.")
for month in months:
    while True:
        try:
            rain = float(input(f"{month}: "))
            rainFalls.append(rain)
            break
        except ValueError:
            print("Error: Input must be a number.")

total = 0
for i in rainFalls:
    total += i
average = total / len(rainFalls)

max_rainfall_month = months[rainFalls.index(max(rainFalls))]
min_rainfall_month = months[rainFalls.index(min(rainFalls))]
print()
print(f"Total rainfall: {total:,.2f}")
print(f"Average rainfall: {average:,.2f}")
print(f"Month with highest rainfall: {max_rainfall_month} {max(rainFalls)}")
print(f"Month with lowest Rainfall:  {min_rainfall_month} {min(rainFalls)}")
