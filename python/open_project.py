import os
import maya.cmds as cmds

projects_file_path = r'Your\Maya\Projects_Directory'


def load_project(*args):
    selected_project = cmds.optionMenu(dropdown_menu, query=True, value=True)
    selected_file = cmds.optionMenu(dropdown_menu_2, query=True, value=True)

    selected_project_path = os.path.join(projects_file_path, selected_project)

    selected_file_path = os.path.join(selected_project_path, selected_file)

    scenes_path = os.path.join(selected_file_path, 'scenes')
    scenes_list = os.listdir(scenes_path)

    highest_version_file = scenes_list[-1]
    file_path_to_load = os.path.join(scenes_path, highest_version_file)

    cmds.file(new=True, force=True)
    cmds.file(file_path_to_load, open=True)


def change_file_path(*args):
    selected_project = cmds.optionMenu("myDropdownMenu", query=True, value=True)

    cmds.optionMenu(dropdown_menu_2, e=True, dai=True)
    files_path = os.path.join(projects_file_path, selected_project)

    for project in os.listdir(files_path):
        cmds.menuItem(label=project, parent=dropdown_menu_2)


# Delete window if it already exists
if cmds.window("myWindow", exists=True):
    cmds.deleteUI("myWindow", window=True)

# Create the main window
mainWindow = cmds.window("myWindow", title="Select Project")
mainLayout = cmds.columnLayout(adjustableColumn=True)

# Both dropdown menus
dropdown_menu = cmds.optionMenu("myDropdownMenu", label="Projects Available", parent=mainLayout, cc=change_file_path)
dropdown_menu_2 = cmds.optionMenu("myDropdownMenu_2", label="Choose File", parent=mainLayout)

# Append menu items of dropdown menu 1
for project in os.listdir(projects_file_path):
    cmds.menuItem(label=project, parent=dropdown_menu)

# Set initial options for dropdown menu 2
selected_project = cmds.optionMenu("myDropdownMenu", query=True, value=True)

files_path = os.path.join(projects_file_path, selected_project)
for project in os.listdir(files_path):
    cmds.menuItem(label=project, parent=dropdown_menu_2)

# Button to load project
button = cmds.button(label="Load Project", parent=mainLayout, command=load_project)

# Show the window
cmds.showWindow(mainWindow)
