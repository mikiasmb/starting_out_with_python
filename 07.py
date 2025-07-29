test1 = float(input("Enter ur first test result: "))
test2 = float(input("Enter ur second test result: "))
final = float(input("Enter ur final exam result: "))

if (0 <= test1 <= 25) and (0 <= test2 <= 25) and (0 <= final <= 50):
    if final >= 25:
        total = int(format(test1 + test2 + final, ".0f"))
        print(f"Total score = {total}")
        if total >= 80:
            grade = "Distinction"
        elif 60 <= total < 80:
            grade = "Credit"
        elif 50 <= total < 60:
            grade = "Pass"
        else:
            grade = "Fail"
    else:
        grade = "Fail"
    print(f"Grade = {grade}")
else:
    print("error")
