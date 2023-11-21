import maya.cmds as cmds
import os


# Function to open and set project directory
def browse_directory(*args):
    directory_path = cmds.fileDialog2(dialogStyle=2, fileMode=3)
    if directory_path:
        cmds.textField(directory_field, edit=True, text=directory_path[0])


# Function to set project
def set_project(selected_directory, folder_name):
    set_project_dir = os.path.join(selected_directory, folder_name)

    if not os.path.exists(set_project_dir):
        os.mkdir(set_project_dir)

    folders_list = ["scenes", "assets", "textures", "ref_images", "scripts"]
    for folder in folders_list:
        folder_dir = os.path.join(set_project_dir, folder)
        if not os.path.exists(folder_dir):
            os.mkdir(folder_dir)

    scenes_dir = os.path.join(set_project_dir, "scenes")

    file_name = folder_name + "_v001.ma"
    save_path = os.path.join(scenes_dir, file_name)
    cmds.file(rn=save_path)
    cmds.file(s=True, f=True, typ="mayaAscii")


# Function to create project folder
def create_project_folder(*args):
    selected_directory = cmds.textField(directory_field, query=True, text=True)
    folder_name = cmds.textField(folder_field, query=True, text=True)

    if selected_directory and folder_name:

        set_project(selected_directory, folder_name)

        # Delete window after project folder is created
        if cmds.window(window_name, exists=True):
            cmds.deleteUI(window_name)

    else:
        cmds.confirmDialog(title="Error", message="Please select a directory and enter a project name.", button=["OK"],
                           defaultButton="OK")


# Create a window
window_name = "myWindow"

# Delete window if it already exists
if cmds.window(window_name, exists=True):
    cmds.deleteUI(window_name)

cmds.window(window_name, title="Choose Directory To Create Project Folder", h=500, w=300)

# Column layout for UI
column_layout = cmds.columnLayout(adjustableColumn=True, rowSpacing=10, columnAttach=["both", 5])

# Row layout for browsing directory
row_layout1 = cmds.rowLayout(numberOfColumns=3, columnWidth3=[100, 400, 100], columnAlign3=["right", "left", "left"])
cmds.text(label="Select Directory:")
directory_field = cmds.textField(editable=True, text="", width=400)
browse_button = cmds.button(label="Browse", width=100, command=browse_directory)
cmds.setParent("..")

# Row layout for folder name
row_layout2 = cmds.rowLayout(numberOfColumns=2, columnWidth2=[100, 400], columnAlign2=["right", "left"])
cmds.text(label="Folder Name:")
folder_field = cmds.textField(editable=True, text="", width=400)
cmds.setParent("..")

# Button to create project folder
set_project_button = cmds.button(label="Set Project", width=500, command=create_project_folder)

# Show window
cmds.showWindow(window_name)
