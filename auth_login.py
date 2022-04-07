import re
import regex
import json


def display_login():
    email = input("Please enter your email: ")

    # check email validity
    while not re.fullmatch(regex.email_validation, email):
        print("⚠️ Please enter a valid email ⚠️")
        email = input("Please enter your email: ")

    password = input("Please enter your password: ")

    # check last name validity
    while not password.isalnum():
        print("⚠️ Please enter a valid password ⚠️")
        password = input("Please confirm your password: ")

    with open("user.json", "r+") as file:
        file_data = json.load(file)
        for user in file_data["users"]:

            if user["email"] == email and user["password"] == password:
                import projects
                projects.display_project_options()
                return

            elif user["email"] != email:
                print("Email is not in the db, please register")
                email = input("Please enter your email: ")

            elif user["password"] != password:
                print("Password is not in the db")
                password = input("Please write your password: ")
