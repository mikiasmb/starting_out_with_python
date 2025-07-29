def main():
    word = input("Enter a word: ").lower()      # get the string
    print(f"Vowels: {vowel(word)}")
    print(f"Consonants: {consonant(word)}")


def vowel(string):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


def consonant(string):
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                  "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    count = 0
    for char in string:
        if char in consonants:
            count += 1
    return count


if __name__ == '__main__':
    main()
