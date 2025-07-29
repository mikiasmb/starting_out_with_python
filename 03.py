total = 0
number = []
run = int(input("Enter the number of times you run around a racetrack: "))

while run <= 0:
    print("error")
    run = int(input("Enter the number of times you run around a racetrack: "))

for i in range(run):
    lap = float(input(f"Enter the lap{i+1} time: "))
    total += lap
    number.append(lap)
    slow = max(number)   # variable.append() is used to add values to the list where in this case our list is number
    fast = min(number)
    average = total / run
print(f"fastest lap time {fast}")
print(f"slowest lap time {slow}")
print(f"average lap time {average:.3f}")
