total = 0
numbers = input("Enter a series of numbers: ")
listed_numbers = list(numbers)  # convert str into list

for num in listed_numbers:
    total += int(num)  # convert to int and add the num to the total

print(f"Total: {total}")
