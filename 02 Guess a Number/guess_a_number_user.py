import random


def guess():
    random_number = random.randint(1, 100)
    guess = 0
    count = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and 100: "))
        if guess < random_number-25:
            print("Sorry, guess again. Too low.")
        elif guess > random_number+25:
            print('Sorry, guess again. Too high.')
        else:
            if guess < random_number:
                print("Sorry guess again. Little bit higher next time.")
            else:
                print("Sorry guess again. Little bit lower next time.")
        count += 1
    print(
        f"Congratulation!!! You have correctly guessed the number {random_number}. Since you take {count} chance, you have won Rs.{int(10000/count)}")


guess()