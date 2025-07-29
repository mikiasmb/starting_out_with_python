numbers = []
total = 0
average = 0
for num in range(20):
    while True:
        try:
            n = float(input("Enter a number: "))
            numbers.append(n)
            total += n
            break
        except ValueError:
            print("Error: input must be a number.")

average = total / len(numbers)

print()
print(f"Lowest number: {min(numbers)}")
print(f"Highest number: {max(numbers)}")
print(f"Total value: {total}")
print(f"Average: {average}")
