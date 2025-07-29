import math
total = 0
days = 7
sleep_debt = 0
average_Sleep = 0
desirable_Sleep = 8

for i in range(days):
    sleep = int(input(f"Day{i+1} how many hours have you slept? "))
    total += sleep
    average_Sleep = total / days
    sleep_debt = average_Sleep - desirable_Sleep

if average_Sleep > desirable_Sleep:
    print("Go outside explore the world don't sleep all day, but good job! no sleep debt.")
elif average_Sleep < desirable_Sleep:
    print(f"Who are you batman? go to bed, {abs(sleep_debt):.0f} hours of sleep debt.")
elif average_Sleep == desirable_Sleep:
    print("Good job! no sleep debt, be consistence.")
print("Remember your average sleep should not be less or greater than 8 hours.")
