import random

max_number = int(input("Please enter your limit: "))


def comp_guess(max_number):
    low = 0
    high = max_number
    feedback = ''

    while feedback != 'c':
        if low != high:  # to evade error caused by randint when low == high
            guessed = random.randint(low, high)

        else:
            guessed = low

        feedback = input(
            f"Is {guessed} too high (H), too low (L), or correct (C): ".lower())

        if feedback == 'h':
            high = guessed - 1

        elif feedback == 'l':
            low = guessed + 1

    print(f"yaaay, {guessed} is the right answer")


comp_guess(max_number)
