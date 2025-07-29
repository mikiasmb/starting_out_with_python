user_input = input("Enter a message: ").upper()
shifting_num = int(input("By how many numbers do you want to shift: "))
alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

encrypted = []
for char in user_input.strip():
    if char in alphabets:
        index = alphabets.index(char)
        new_index = (shifting_num + index) % len(alphabets)  # Corrected wrapping logic
        encrypted.append(alphabets[new_index])
    else:
        encrypted.append(char)  # Non-alphabetic characters remain unchanged

print("".join(encrypted))
