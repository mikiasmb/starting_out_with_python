import random


def main():
    max_question = 5
    for i in range(max_question):
        print(question())


def question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = f"{a} + {b} = "
    return c


main()
