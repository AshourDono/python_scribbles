import json


def view_all_projects():
    with open("proj.json", "r+") as file:
        file_data = json.load(file)
        for project in file_data["projects"]:
            print(project)

        import projects
        projects.display_project_options()
