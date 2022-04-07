project_options = {
    1: "Create a project",
    2: "View a project",
    3: "Edit a project",
    4: "Delete a project",
}


print("Welcome to projects")


def select_project_option(user_choice):
    while not user_choice in project_options.keys():
        print("Sorry, wrong entry")
        user_choice = int(
            input("Please enter your option: "))

    if user_choice == 1:
        import project_create
        project_create.create_project()
    elif user_choice == 2:
        import project_view
        project_view.view_all_projects()
    elif user_choice == 3:
        import project_edit
        project_edit.edit_project()
    elif user_choice == 4:
        import project_delete
        project_delete.delete_project()


def display_project_options():

    for key, value in project_options.items():
        print(key, value)

    user_choice = int(
        input("Please enter your option: "))

    select_project_option(user_choice)


display_project_options()
