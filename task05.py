user_input = input('Please enter a string: ')


def reversed_string(user_input):
    print("".join(reversed(user_input)))
    print(user_input[::-1])


reversed_string(user_input)
