import random

max_number = int(input("please choose max number: "))


def guess(max_number):
    random_number = random.randint(0, max_number)
    guess_number = 0

    while random_number != guess_number:
        guess_number = int(
            input(f"please enter your guess between 0 and {max_number}: "))

        if guess_number < random_number:
            print("sorry, guess again, too low")

        elif guess_number > random_number:
            print("sorry, guess again, too high")

    print(f"yaaay, you guessed it right, it is {random_number}")


guess(max_number)
