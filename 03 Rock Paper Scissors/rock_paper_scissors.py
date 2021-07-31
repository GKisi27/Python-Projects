import random


def play():
    user = input("Type 'r' for rock, 'p' for paper and 's' for scissors: \n")
    rps = ["r", "p", "s"]
    computer = random.choice(rps)

    while user not in rps:
        print(f"{user} is not an option. Try again.")
        user = input("Type 'r' for rock, 'p' for paper and 's' for scissors: \n")

    if user == computer:
        print("It's a tie.")

    elif is_win(user, computer):
        print("You Won!!!")

    else:
        print("You Lost!!")


def is_win(player, opponent):
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True


play()