R = float(input("Enter the length of the row, in feet: "))
E = float(input("Enter the amount of space used by an end-post assembly, in feet: "))
S = float(input("Enter the amount of space between the vines, in feet: "))
# calculating
V = (R - 2 * E) / S
# displaying
print(f"The number of grapevines that will fit in the row is {V:,.1f} feet")