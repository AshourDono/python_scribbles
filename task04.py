entered_number = int(input("please enter a number: "))


def fizz_buzz(entered_number):
    if entered_number % 3 == 0 and entered_number % 5 == 0:
        print("fizzbuzz")

    elif entered_number % 3 == 0:
        print("fizz")

    elif entered_number % 5 == 0:
        print("buzz")

    else:
        print("Not divisable by 3 or 5")


fizz_buzz(entered_number)
