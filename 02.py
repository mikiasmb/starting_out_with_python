length1 = float(input("Enter length of 1st rectangle: "))
width1 = float(input("Enter width of 1st rectangle: "))
length2 = float(input("Enter length of 2nd rectangle: "))
width2 = float(input("Enter width of 2nd rectangle: "))

area1 = length1 * width1
area2 = length2 * width2

print(f"Area1 = {area1}")
print(f"Area2 = {area2}")

if area1 > area2:
    print("Area1 is greater than Area2")
elif area1 < area2:
    print("Area2 is greater than Area1")
else:
    print("Both areas are equal")
