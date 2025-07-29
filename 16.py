import random
count_even = 0
count_odd = 0

for i in range(100):
    number = random.randint(1, 100)
    even = number % 2
    if even == 0:
        count_even += 1
    else:
        count_odd += 1

print(f"{count_even} even numbers.")
print(f"{count_odd} odd numbers.")
