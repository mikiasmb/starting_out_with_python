seconds = int(input("Enter a number of seconds: "))

sec = seconds % 60
minute = format(seconds // 60, ',')
hour = format(seconds // 3600, ',')
day = format(seconds // 86400, ',')

if 60 <= seconds < 3600:
    print(f"{minute} minute and {sec} second.")
elif 3600 <= seconds < 86400:
    print(f"{hour} hour, {minute} minute and {sec} second.")
elif seconds >= 86400:
    print(f"{day} day, {hour} hour, {minute} minute and {sec} second.")
