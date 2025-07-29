ht = "\t"    # horizontal tab
p = int(input("Starting number of organisms: "))
while p < 0:
    p = int(input("Starting number of organisms: "))
r = float(input("Average daily increase(%): "))
while r < 0:
    r = float(input("Average daily increase(%): "))
t = int(input("NUmber of days to multiply: "))
while t < 0:
    t = int(input("Number of days to multiply: "))
print(f"Day Approximate{ht*2}Population")
r = r / 100

for i in range(0, t):
    a = p * (1 + r)**i
    print(f"{i+1}{ht*5}{a}")
