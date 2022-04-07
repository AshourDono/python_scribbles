import json


class Project():
    def __init__(self) -> None:
        self.project_title = ""
        self.project_details = ""
        self.project_target = ""
        self.project_id = ""
        self.project_info = {"projects": []}
        self.project_data = {}
        self.project_options = {
            1: "Create a project",
            2: "View a project",
            3: "Edit a project",
            4: "Delete a project",
            5: "Logout"
        }
        self.user_project_choice = 0

    def display_project_options(self):
        print("Welcome to projects")

        for key, value in self.project_options.items():
            print(key, value)

        self.user_project_choice = int(
            input("Please enter your option: "))

        while not self.user_project_choice in self.project_options.keys():
            print("Sorry, wrong entry")
            self.user_project_choice = int(
                input("Please enter your option: "))

        if self.user_project_choice == 1:
            self.create_project()
        elif self.user_project_choice == 2:
            self.view_all_projects()
        elif self.user_project_choice == 3:
            self.edit_project()
        elif self.user_project_choice == 4:
            self.delete_project()
        elif self.user_project_choice == 5:
            self.logout()

    def create_project(self):
        self.project_title = input("Please enter your project title: ")

        # check project title validity
        while not self.project_title.isalpha() or len(self.project_title) < 5:
            print("⚠️ Please enter a valid project title ⚠️")
            self.project_title = input("Please enter your project details: ")

        self.project_data["project_title"] = self.project_title

        self.project_details = input("Please enter your project details: ")
        self.project_data["project_details"] = self.project_details

        self.project_target = input("Please enter your project target: ")

        # check project target validity
        while not self.project_target.isdecimal():
            print("⚠️ Please enter a valid project target ⚠️")
            self.project_target = input("Please enter your project target: ")

        self.project_data["project_target"] = self.project_target

        self.project_data["id"] = self.project_data.get(
            "id", len(self.project_info["projects"])) + 1

        with open("proj.json", "r+") as file:
            file_data = json.load(file)
            file_data["projects"].append(self.project_data)
            file.seek(0)
            json.dump(file_data, file, indent=4)

        self.display_project_options()

    def view_all_projects(self):
        with open("proj.json", "r+") as file:
            file_data = json.load(file)
            for project in file_data["projects"]:
                print(project)

            self.display_project_options()

    def edit_project(self):
        self.project_id = input(
            "Please enter id of project you want to edit: ")

        with open("proj.json", "r+") as file:
            file_data = json.load(file)
            for project in file_data["projects"]:
                if project["id"] == int(self.project_id):
                    self.project_title = input(
                        "Please enter your project title: ")

                    # check project title validity
                    while not self.project_title.isalpha() or len(self.project_title) < 5:
                        print("⚠️ Please enter a valid project title ⚠️")
                        self.project_title = input(
                            "Please enter your project title: ")

                    project["project_title"] = self.project_title

                    self.project_details = input(
                        "Please enter your project details: ")
                    project["project_details"] = self.project_details

                    self.project_target = input(
                        "Please enter your project target: ")

                    # check project target validity
                    while not self.project_target.isdecimal():
                        print("⚠️ Please enter a valid project target ⚠️")
                        self.project_target = input(
                            "Please enter your project target: ")

                    project["project_target"] = self.project_target

                    file.truncate(0)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)
                    file.close()

                    print("Project edited Successfully")

            else:
                print("This id is not valid")

            self.display_project_options()

    def delete_project(self):
        self.project_id = input(
            "Please enter id of project you want to delete: ")

        with open("proj.json", "r+") as file:
            file_data = json.load(file)
            for project in file_data["projects"]:
                if project["id"] == int(self.project_id):
                    # del project
                    file_data["projects"].pop(project["id"]-1)
                    file.truncate(0)
                    file.seek(0)
                    json.dump(file_data, file, indent=4)
                    file.close()
                    print("Project deleted Successfully")
            else:
                print("This id is not valid")

            self.display_project_options()

    def logout(self):
        import User
        User.User.display_options()
