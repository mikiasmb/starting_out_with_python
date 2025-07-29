c = 4.2  # calories
t = "\t"
print(f"Minutes{t*2}Calories burned")
print("---------------------------")
for i in range(10, 31, 5):
    burned = i * c
    print(f"{i}{t*3}{burned}")
