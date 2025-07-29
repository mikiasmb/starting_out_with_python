import random


def main():
    print("Dice roll")
    print("Enter how many times do you want to roll.\n(q to quit)")
    while True:
        try:
            user_input = input(": ")
            if user_input.lower() == "q":
                break
            else:
                number_of_throws = int(user_input)
                result(roll(number_of_throws))
        except ValueError:
            print("Error: Input must be a positive number or q.")


def roll(throw):
    throws = []
    for i in range(throw):
        throws.append(random.randint(1, 6))
    return throws


def result(a):
    for i in a:
        print(i)


if __name__ == '__main__':
    main()
