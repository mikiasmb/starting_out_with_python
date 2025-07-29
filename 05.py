# Lists to store the letters and their corresponding numbers
letters = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"],
    ["J", "K", "L"],
    ["M", "N", "O"],
    ["P", "Q", "R", "S"],
    ["T", "U", "V"],
    ["W", "X", "Y", "Z"]
]

numbers = ["2", "3", "4", "5", "6", "7", "8", "9"]

# Get the input from the user
phone_number = input("Enter a 10-character telephone number (e.g., 555-GET-FOOD): ")

# Initialize an empty string to store the converted number
converted_number = ""

# Loop through each character in the input phone number
for char in phone_number:
    if char.isalpha():  # Check if the character is a letter
        for i in range(len(letters)):
            if char.upper() in letters[i]:
                converted_number += numbers[i]
                break
    else:
        converted_number += char  # If it's not a letter, keep it as is

# Print the converted phone number
print("Converted phone number:", converted_number)
