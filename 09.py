number = int(input("Enter a pocket number: "))
eo = number % 2       # checking ever or odd
if 0 <= number <= 36:
    if eo == 0:
        if 1 <= number <= 10:
            print("black")
        elif 11 <= number <= 18:
            print("red")
        elif 19 <= number <= 28:
            print("black")
        elif 29 <= number <= 36:
            print("red")
        elif 0 == number:
            print("green")
    elif eo == 1:
        if 1 <= number <= 10:
            print("red")
        elif 11 <= number <= 18:
            print("black")
        elif 19 <= number <= 28:
            print("red")
        elif 29 <= number <= 36:
            print("black")
else:
    print("error")
