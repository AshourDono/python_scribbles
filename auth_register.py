import re
import json
import regex


users = []
user_info = {"users": []}
user_data = {}


def display_register():

    first_name = input("Please enter your first name: ")

    # check first name validity
    while not first_name.isalpha() or len(first_name) < 3:
        print("⚠️ Please enter a valid first name ⚠️")
        first_name = input("Please enter your first name: ")

    user_data["first_name"] = first_name
    last_name = input("Please enter your last name: ")

    # check last name validity
    while not last_name.isalpha() or len(first_name) < 3:
        print("⚠️ Please enter a valid last name ⚠️")
        last_name = input("Please enter your last name: ")

    user_data["last_name"] = last_name
    email = input("Please enter your email: ")

    # check email validity
    while not re.fullmatch(regex.email_validation, email):
        print("⚠️ Please enter a valid email ⚠️")
        email = input("Please enter your email: ")

    user_data["email"] = email
    password = input("Please enter your password: ")

    # check last name validity
    while not password.isalnum() or len(password) < 6:
        print("⚠️ Please enter a valid password ⚠️")
        password = input("Please confirm your password: ")

    user_data["password"] = password
    confirm_password = input("Please confirm your password: ")

    # check confirm password validity
    while password != confirm_password:
        print("⚠️ Passwords do not match ⚠️")
        confirm_password = input("Please enter your password: ")

    user_data["confirm_Password"] = confirm_password
    mobile_phone = input("Please enter your phone number: ")

    # check email validity
    while not re.fullmatch(regex.mobile_number_validation, mobile_phone):
        print("⚠️ Please enter a valid mobile phone ⚠️")
        mobile_phone = input("Please enter your phone number: ")

    user_data["mobile_phone"] = mobile_phone
    user_data["id"] = user_data.get("id", len(users)) + 1

    with open("user.json", "r+") as file:
        file_data = json.load(file)
        file_data["users"].append(user_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)

    import main_menu
    main_menu.display_options()
