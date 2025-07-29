import matplotlib.pyplot as plt
readfile = open("expenses.txt", "r")
values = readfile.readlines()
plt.title("Last month expenses.")
expenses = ["Rent", "Gas", "Food", "Clothing", "Car payment", "Misc"]
colors = ["b", "k", "g", "c", "y", "r"]
plt.pie(values, labels=expenses, colors=colors)
plt.show()
