import json


def delete_project():
    project_id = input("Please enter id of project you want to delete: ")

    with open("proj.json", "r+") as file:
        file_data = json.load(file)
        for project in file_data["projects"]:
            if project["id"] == int(project_id):
                # del project
                file_data["projects"].pop(project["id"]-1)
                file.truncate(0)
                file.seek(0)
                json.dump(file_data, file, indent=4)
                file.close()
                print("Project deleted Successfully")
        else:
            print("This id is not valid")

        import projects
        projects.display_project_options()
