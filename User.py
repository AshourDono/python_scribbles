import re
import json
from Project import Project


class User(Project):
    def __init__(self) -> None:
        self.options = {
            1: "Login",
            2: "Register",
            3: "Exit"
        }
        self.user_choice = 0
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.password = ""
        self.confirm_password = ""
        self.mobile_phone = ""
        self.email_validation = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        self.mobile_number_validation = '^01[0125]\d{8}$'
        self.user_info = {"users": []}
        self.user_data = {}

    def display_options(self):
        for key, value in self.options.items():
            print(key, value)

        self.user_choice = int(
            input("\nPlease enter your option: "))

        while not self.user_choice in self.options.keys():
            print("Sorry, wrong entry")
            self.user_choice = int(
                input("\nPlease enter your option: "))

        if self.user_choice == 1:
            self.display_login()
        elif self.user_choice == 2:
            self.display_register()
        elif self.user_choice == 3:
            self.exit()

    def display_login(self):
        self.email = input("Please enter your email: ")

        # check email validity
        while not re.fullmatch(self.email_validation, self.email):
            print("⚠️ Please enter a valid email ⚠️")
            self.email = input("Please enter your email: ")

        self.password = input("Please enter your password: ")

        # check last name validity
        while not self.password.isalnum():
            print("⚠️ Please enter a valid password ⚠️")
            self.password = input("Please confirm your password: ")

        with open("user.json", "r+") as file:
            file_data = json.load(file)
            for user in file_data["users"]:

                if user["email"] == self.email and user["password"] == self.password:
                    project = Project()
                    project.display_project_options()
                    return

                elif user["email"] != self.email:
                    print("Email is not in the db, please register")
                    self.email = input("Please enter your email: ")

                elif user["password"] != self.password:
                    print("Password is not in the db")
                    self.password = input("Please write your password: ")

    def display_register(self):

        self.first_name = input("Please enter your first name: ")

        # check first name validity
        while not self.first_name.isalpha() or len(self.first_name) < 3:
            print("⚠️ Please enter a valid first name ⚠️")
            self.first_name = input("Please enter your first name: ")

        self.user_data["first_name"] = self.first_name
        self.last_name = input("Please enter your last name: ")

        # check last name validity
        while not self.last_name.isalpha() or len(self.last_name) < 3:
            print("⚠️ Please enter a valid last name ⚠️")
            self.last_name = input("Please enter your last name: ")

        self.user_data["last_name"] = self.last_name
        self.email = input("Please enter your email: ")

        # check email validity
        while not re.fullmatch(self.email_validation, self.email):
            print("⚠️ Please enter a valid email ⚠️")
            self.email = input("Please enter your email: ")

        self.user_data["email"] = self.email
        self.password = input("Please enter your password: ")

        # check last name validity
        while not self.password.isalnum() or len(self.password) < 6:
            print("⚠️ Please enter a valid password ⚠️")
            self.password = input("Please confirm your password: ")

        self.user_data["password"] = self.password
        self.confirm_password = input("Please confirm your password: ")

        # check confirm password validity
        while self.password != self.confirm_password:
            print("⚠️ Passwords do not match ⚠️")
            self.confirm_password = input("Please enter your password: ")

        self.user_data["confirm_Password"] = self.confirm_password
        self.mobile_phone = input("Please enter your phone number: ")

        # check email validity
        while not re.fullmatch(self.mobile_number_validation, self.mobile_phone):
            print("⚠️ Please enter a valid mobile phone ⚠️")
            self.mobile_phone = input("Please enter your phone number: ")

        self.user_data["mobile_phone"] = self.mobile_phone
        self.user_data["id"] = self.user_data.get(
            "id", len(self.user_info["users"])) + 1

        with open("user.json", "r+") as file:
            file_data = json.load(file)
            file_data["users"].append(self.user_data)
            file.seek(0)
            json.dump(file_data, file, indent=4)

        self.display_options()

    def exit(self):
        exit()


user = User()
user.display_options()
