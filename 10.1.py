def main():
    try:
        num = int(input("Enter how many players are playing: "))
        file = open("golf.txt", "w")
        for i in range(1, num+1):
            print(f"Enter the data for player #{i}: ")
            name = input(f"Name: ")
            score = input("Score: ")
            file.write(name + "\n")
            file.write(score + "\n")
        file.close()
        print("File is saved to golf.txt.")
    except ValueError:
        print("Error: Invalid input. \nInput must be int.")


if __name__ == '__main__':
    main()
