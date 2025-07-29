import random


def main():
    print("Rock, Paper, Scissors Game")
    computer = computer_choice()
    player = player_choice()
    computer_output, player_output = output(computer, player)
    print(computer_output)
    print(player_output)
    print(game(computer, player))


def computer_choice():
    computer = random.randint(1, 3)
    if computer == 1:
        return "Rock"
    elif computer == 2:
        return "Paper"
    elif computer == 3:
        return "Scissors"


def player_choice():
    print("Select one to play")
    print("1.Rock \n2.Paper \n3.Scissors")
    player = int(input("Enter: "))
    while player not in [1, 2, 3]:
        player = int(input("Enter: "))
    if player == 1:
        return "Rock"
    elif player == 2:
        return "Paper"
    elif player == 3:
        return "Scissors"


def output(c, p):
    computer = f"Computer choice {c}"
    player = f"Player choice {p}"
    return computer, player


def game(c, p):
    if (c == "Paper" and p == "Rock") or (c == "Rock" and p == "Paper"):
        return "Paper wraps Rock"
    elif (c == "Rock" and p == "Scissors") or (c == "Scissors" and p == "Rock"):
        return "Rock smashes Scissors"
    elif (c == "Scissors" and p == "Paper") or (c == "Paper" and p == "Scissors"):
        return "Scissors cut Paper"
    elif c == p:
        return "tie"


if __name__ == '__main__':
    main()
