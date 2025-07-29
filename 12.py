user_input = input("Enter: ")
words = user_input.split()
pig_latin_word = []
for word in words:
    pig_latin_word = [word[1:] + word[0] + "ay" if len(word) > 1 else word + "ay" for word in words]

pig_latin_word = " ".join(pig_latin_word)
print(pig_latin_word)
