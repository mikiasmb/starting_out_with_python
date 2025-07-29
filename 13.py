import random
# Open the file and read the responses
readfile = open("8_ball_responses.txt", "r")
responses = [line.strip() for line in readfile.readlines()]  # Strip each line

# Prompt the user to ask a yes or no question
print("Ask yes or no question.")
user_question = input(": ")

# Print a random response
print(random.choice(responses))
