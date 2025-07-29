total = 0
fast = float("inf")
slow = 0
run = int(input("Enter the number of times you run around a racetrack: "))

while run <= 0:
    print("error")
    run = int(input("Enter the number of times you run around a racetrack: "))

for i in range(run):
    lap = float(input(f"Enter the lap{i+1} time: "))
    total += lap
    if lap > slow:
        slow = lap
    if lap < fast:
        fast = lap
    average = total / run

print(f"fastest lap time {fast}")
print(f"slowest lap time {slow}")
print(f"average lap time {average:.3f}")
