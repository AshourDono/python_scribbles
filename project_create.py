import json


projects_array = []
project_info = {"projects": []}
project_data = {}


def create_project():
    project_title = input("Please enter your project title: ")

    # check project title validity
    while not project_title.isalpha() or len(project_title) < 5:
        print("⚠️ Please enter a valid project title ⚠️")
        project_title = input("Please enter your project details: ")

    project_data["project_title"] = project_title

    project_details = input("Please enter your project details: ")
    project_data["project_details"] = project_details

    project_target = input("Please enter your project target: ")

    # check project target validity
    while not project_target.isdecimal():
        print("⚠️ Please enter a valid project target ⚠️")
        project_target = input("Please enter your project target: ")

    project_data["project_target"] = project_target

    project_data["id"] = project_data.get("id", len(projects_array)) + 1

    with open("proj.json", "r+") as file:
        file_data = json.load(file)
        file_data["projects"].append(project_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)

    import projects
    projects.display_project_options()
