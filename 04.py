speed = int(input("What is the speed of the vehicle in mph? "))
time = int(input("How many hours has it traveled? "))
print("Hour\tDistance Traveled")
print("-------------------------")
for i in range(0, time):
    distance = speed * (i + 1)
    print(f"{i + 1}\t\t\t{distance}")
