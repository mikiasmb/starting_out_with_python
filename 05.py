import random
nums = dict()
for i in range(100):
	random_nums = random.randint(1, 10)
	if random_nums in nums:
		nums[random_nums] += 1
	else:
		nums[random_nums] = 1

sorted_numbers = dict(sorted(nums.items()))
total = sum(sorted_numbers.values())

print("Numbers\t\tFrequency")
print("---------------------")
for k, v in sorted_numbers.items():
	print(f"{k}\t\t\t\t{v}")

print("Total count:", total)
