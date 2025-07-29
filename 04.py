# List of characters in the Morse code table
characters = [' ', ',', '.', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Corresponding Morse codes for the characters
morse_codes = [' ', '– – . . – –', '. – . – . –', '. . – – . .', '– – – – –',
               '. – – – –', '. . – – –', '. . . – –', '. . . . –', '. . . . .',
               '– . . . .', '– – . . .', '– – – . .', '– – – – .', '. –',
               '– . . .', '– . – .', '– . .', '.', '. . – .', '– – .', '. . . .',
               '. .', '. – – –', '– . –', '. – . .', '– –', '– .', '– – –',
               '. – – .', '– – . –', '. – .', '. . .', '–', '. . –', '. . . –',
               '. – –', '– . . –', '– . – –', '– – . .']

# Prompt the user to enter a string
user_input = input("Enter a string to convert to Morse code: ")

# Convert the input string to uppercase
user_input = user_input.upper()

# Initialize an empty list to store Morse code translations
morse_code_translation = []

# Translate each character to Morse code
for char in user_input:
    if char in characters:
        # Find the index of the character in the characters list
        index = characters.index(char)
        # Append the corresponding Morse code to the translation list
        morse_code_translation.append(morse_codes[index])

for code in morse_code_translation:
    print(code, end="")
