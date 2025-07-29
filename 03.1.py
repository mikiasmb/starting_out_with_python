# Dictionary with codes
codes = {
    'A': '%', 'a': '9',
    'B': '@', 'b': '#',
    'C': '$', 'c': '1',
    'D': '^', 'd': '2',
    'E': '&', 'e': '3',
    'F': '*', 'f': '4',
    'G': '(', 'g': '5',
    'H': ')', 'h': '6',
    'I': '-', 'i': '7',
    'J': '_', 'j': '8',
    'K': '+', 'k': '=',
    'L': '{', 'l': '[',
    'M': '}', 'm': ']',
    'N': '|', 'n': '\\',
    'O': ':', 'o': ';',
    'P': '"', 'p': "'",
    'Q': '<', 'q': ',',
    'R': '>', 'r': '.',
    'S': '?', 's': '/',
    'T': '0', 't': '!',
    'U': '1', 'u': '2',
    'V': '3', 'v': '4',
    'W': '5', 'w': '6',
    'X': '7', 'x': '8',
    'Y': '9', 'y': '0',
    'Z': '~', 'z': '`'
}


# Function to find key by value
def find_key_by_value(value, dictionary):
    for current_key in dictionary:  # Renamed variable to avoid shadowing
        if dictionary[current_key] == value:
            return current_key
    return None


# Open the encrypted file and read its contents
with open("encrypted_text.txt", "r") as encrypted_file:
    all_content = encrypted_file.read()

# Decrypt the content
decrypted_text = ""
for line in all_content:
    # Check if the character is a value in the codes dictionary
    for char in line:
        if char in codes.values():
            corresponding_key = find_key_by_value(char, codes)  # Renamed variable to avoid shadowing
            # decrypted_text += corresponding_key if corresponding_key else char
        else:
            decrypted_text += char  # Add characters not in the codes as is

# Print the decrypted text
print(decrypted_text)
