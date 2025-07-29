user_input = input("Enter a message: ").upper()
shifting_num = int(input("By how many num do you want to shift: "))
alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

encrypted = []
for char in user_input.strip():
    try:
        if char in alphabets:
            index = alphabets.index(char)
            if (shifting_num + index) >= len(alphabets):
                new_index = (shifting_num + index) - (len(alphabets))
                encrypted.append(alphabets[new_index])
            else:
                new_index = shifting_num + index
                encrypted.append(alphabets[new_index])
        else:
            encrypted.append(char)
    except ValueError:
        print("Error invalid input.")

print("".join(encrypted))
