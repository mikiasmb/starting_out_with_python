def main():
    try:
        num = int(input("Enter how many words you want to write: "))
        file = open("words.txt", "w")
        for i in range(num):
            words = input("Enter a word: ")
            file.write(words + "\n")
        print("File is saved to words.txt.")
        file.close()
    except ValueError:
        print("Error: Invalid input. \nInput must be int.")


if __name__ == '__main__':
    main()
