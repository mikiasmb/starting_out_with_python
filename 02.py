import random
lottery_number = []
for i in range(7):
    lottery_number.append(random.randint(0, 9))
numbers = ""
for num in lottery_number:
    numbers += str(num)
print(f"Lottery number: {numbers}")
