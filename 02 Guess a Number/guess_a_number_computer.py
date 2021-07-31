import random


def computer_guess():
    low = 1
    high = 100
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could be high because low=high
        feedback = input(
            f"Is {guess} too high (H), too low (L) or correct (C)?? ").lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
    print(f"Computer guessed the number correctly. It's {guess}.")


computer_guess()