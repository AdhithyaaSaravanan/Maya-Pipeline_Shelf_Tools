import maya.cmds as cmds
import os

file_path = cmds.file(q=True, sn=True)
directory = os.path.dirname(file_path)
files = os.listdir(directory)

menu_dropdown = []
all_versions = []
for file_obj in files:

    # Check if file is a .ma file.
    # This check shouldn't be necessary as manual file creation
    # shouldn't happen in these directories, but just to be safe.
    if file_obj.endswith('.ma'):
        name_split = file_obj.split('.')
        assert len(name_split) == 2

        file_name = name_split[0]
        menu_dropdown.append(file_name[-3:])
        all_versions.append(file_name)


def load_selected_version(*args):
    # Get selected version
    selected_version = cmds.optionMenu("myDropdownMenu", query=True, value=True)

    selected_file = None
    for file_name in all_versions:
        if selected_version in file_name:
            selected_file = file_name

    assert selected_file is not None
    file_open_path = os.path.abspath((os.path.join(directory, selected_file + ".ma")))

    cmds.file(new=True, force=True)
    cmds.file(file_open_path, open=True)


# Delete window if it already exists
if cmds.window("myWindow", exists=True):
    cmds.deleteUI("myWindow", window=True)

mainWindow = cmds.window("myWindow", title="Select Version")
mainLayout = cmds.columnLayout(adjustableColumn=True)

# Create dropdown menu
dropdown_menu = cmds.optionMenu("myDropdownMenu", label="Versions Available", parent=mainLayout)

# Append menu items
for version in menu_dropdown:
    cmds.menuItem(label=version, parent=dropdown_menu)

# Set current selected value to the highest version
cmds.optionMenu(dropdown_menu, edit=True, select=int(menu_dropdown[-1]))

# Button to load file
button = cmds.button(label="Load File", parent=mainLayout, command=load_selected_version)

# Show the window
cmds.showWindow(mainWindow)
