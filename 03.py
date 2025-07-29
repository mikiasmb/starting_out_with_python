# Prompt the user to enter a date in the format 'mm/dd/yyyy'
date = input("Enter the date in the form of 'mm/dd/yyyy': ")

# Split the date string into month, day, and year
split_date = date.split("/")

# List of month names corresponding to their numerical values
months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

# Extract the month, day, and year from the split date
# Subtract 1 from month index to match the zero-based index of the months list
month_index = int(split_date[0]) - 1
day = split_date[1]
year = split_date[2]

# Get the month name from the months list
month_name = months[month_index]

# Print the formatted date
print(f"{month_name} {int(day)}, {year}")
