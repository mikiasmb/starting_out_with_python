print("Year\tTuition")
print("---------------")
tuition = 8000
for i in range(1, 6):
    tuition += tuition * 0.03
    print(f"{i}\t\t${tuition:,.2f}")
