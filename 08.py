infile = open("C:/Users/Mikias/Desktop/starting out with python/unit 6/words.txt", "r")

total = 0
count = 0
longest_word = ""
for line in infile:
    # Count total characters in the line
    total += len(line.strip())  # strip() removes leading/trailing whitespace including newline characters

    # Split the line into words and check for the longest word
    words = line.split()
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    count += 1  # Count the number of lines

average = total / count  # Calculate average characters per line
infile.close()

print("Total characters (excluding newlines & including space):", total)
print("Average characters per line:", average)
print("The longest word is:", longest_word)
