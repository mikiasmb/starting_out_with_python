numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
valid_numbers = [num for num in numbers if 0 <= num <= 100]
total = 0
for i in valid_numbers:
    total += i
average = total / len(valid_numbers)
print(f"Total: {total}")
print(f"Average: {average:,.2f}")
