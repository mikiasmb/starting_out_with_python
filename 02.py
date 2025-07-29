def main():
    word = input("Enter a word: ")
    times = int(input("How many times to repeat: "))
    print(repeat(word, times))


def repeat(word, times):
    new = word * times
    return new


main()
