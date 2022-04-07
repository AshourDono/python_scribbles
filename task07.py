from validate_email import validate_email

user_name = input("Please enter your name: ")


def credentials(user_name):
    while not user_name.isalpha():
        user_name = input("Please enter your name: ")

    user_email = input("Please enter your email: ")

    is_valid = validate_email(
        user_email, check_format=True, check_dns=True)

    while not is_valid:
        print("Sorry, Email is not valid")
        user_email = input("Please enter your email: ")
        is_valid = validate_email(
            user_email, check_format=True, check_dns=True)

    print(f"your name is {user_name}")
    print(f"your email is {user_email}")


credentials(user_name)
