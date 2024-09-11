with open("text1.txt", "r") as file:
    contents = file.read().strip()
    words = contents.split()
unique_words = set(w for w in words)
print(f"Unique words are: \n{unique_words}")
