options = {
    1: "Login",
    2: "Register"
}


def select_option(user_choice):
    while not user_choice in options.keys():
        print("Sorry, wrong entry")
        user_choice = int(
            input("\nPlease enter your option (1 for Login, 2 for register): "))

    if user_choice == 1:
        import auth_login
        auth_login.display_login()
    elif user_choice == 2:
        import auth_register
        auth_register.display_register()


def display_options():

    for key, value in options.items():
        print(key, value)

    user_choice = int(
        input("\nPlease enter your option (1 for Login, 2 for register): "))

    select_option(user_choice)


display_options()
