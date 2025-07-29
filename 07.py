def main():
    correct, user = getting_answer()
    print()
    checking_answers(correct, user)


def getting_answer():
    correct_answers = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B",
                       "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
    user_answer = []
    for i in range(len(correct_answers)):
        while True:
            try:
                answer = str(input(f"Enter #{i+1} answer: ")).upper()
                if answer not in correct_answers:
                    raise ValueError
                else:
                    user_answer.append(answer)
                break
            except ValueError:
                print("Error: Input must be A, B, C or D")
    return correct_answers, user_answer


def checking_answers(correct, user):
    correct_count = 0
    incorrect_count = 0
    incorrect_list = []
    incorrect_answer = ""

    for i in range(len(correct)):
        if correct[i] == user[i]:
            correct_count += 1
        else:
            incorrect_list.append(i+1)
            incorrect_count += 1
    print()
    if correct_count >= 15:
        print("you have passed the exam.")
    else:
        print("You have failed the exam.")

    for j in range(len(incorrect_list)):
        if j != 0:
            incorrect_answer += ","
        incorrect_answer += str(incorrect_list[j])

    print(f"Question number {incorrect_answer} answer is incorrect.")
    print(f"Total correct answered: {correct_count}")
    print(f"Total incorrect answered: {incorrect_count}")


if __name__ == '__main__':
    main()
