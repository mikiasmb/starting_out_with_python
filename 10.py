user_input = input("Enter a word: ")
max_count = 0
most_frequent_char = ""

for i in range(len(user_input)):
    count = 0
    if user_input[i] in user_input[:i]:
        for j in range(len(user_input)):
            if user_input[i] == user_input[j]:
                count += 1

        if count > max_count:
            max_count = count
            most_frequent_char = user_input[i]

print(f"The most frequent character is '{most_frequent_char}' which appears {max_count} times.")
