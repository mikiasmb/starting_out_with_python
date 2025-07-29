def main():
    ave = calc_average()
    print(f"Average - {ave}")
    print(f"Grade - {determine_grade(ave)}")


def calc_average():
    total = 0
    for i in range(5):
        score = int(input(f"Enter test{i+1} score: "))
        total += score
    average = total / 5
    return average


def determine_grade(average):
    if 90 <= average <= 100:
        grade = "A"
    elif 80 <= average <= 89:
        grade = "B"
    elif 70 <= average <= 79:
        grade = "C"
    elif 60 <= average <= 69:
        grade = "D"
    else:
        grade = "F"
    return grade


if __name__ == '__main__':
    main()
