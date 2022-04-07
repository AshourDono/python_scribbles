import json


def edit_project():
    project_id = input("Please enter id of project you want to edit: ")

    with open("proj.json", "r+") as file:
        file_data = json.load(file)
        for project in file_data["projects"]:
            if project["id"] == int(project_id):
                project_title = input("Please enter your project title: ")

                # check project title validity
                while not project_title.isalpha() or len(project_title) < 5:
                    print("⚠️ Please enter a valid project title ⚠️")
                    project_title = input(
                        "Please enter your project title: ")

                project["project_title"] = project_title

                project_details = input(
                    "Please enter your project details: ")
                project["project_details"] = project_details

                project_target = input("Please enter your project target: ")

                # check project target validity
                while not project_target.isdecimal():
                    print("⚠️ Please enter a valid project target ⚠️")
                    project_target = input(
                        "Please enter your project target: ")

                project["project_target"] = project_target

                file.seek(0)
                json.dump(file_data, file, indent=4)
                file.close()

                print("Project edited Successfully")

        else:
            print("This id is not valid")

        import projects
        projects.display_project_options()
