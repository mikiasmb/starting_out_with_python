import random


def main():
    file = open("random_numbers.txt", "w")
    try:
        num = int(input("Enter how many random numbers the file will hold: "))
        for i in range(num):
            number = random.randint(1, 500)
            file.write(f"{number}\n")
        file.close()
    except ValueError:
        print(f"Error: Invalid input. \nInput must be an int.")


if __name__ == '__main__':
    main()
