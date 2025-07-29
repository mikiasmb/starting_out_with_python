user_input = input("Enter: ")
words = user_input[0]

for char in user_input[1:]:
    if char.isupper():
        words += " "
    words += char

words = words.lower()
words = words.capitalize()

print(words)
