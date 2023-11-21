import os
import maya.cmds as cmds


file_path = cmds.file(q=True, sn=True)

file_name = os.path.basename(file_path)
name_split = file_name.split('.')

assert len(name_split) == 2
version_no = name_split[0][-3:]

assert version_no.isdigit()

next_version_no = int(version_no) + 1
formatted_version_no = "v{:03d}".format(next_version_no)

# Remove version no and file extension to add new version no
new_file_name = file_name[:-7] + formatted_version_no + ".ma"
new_save_path = os.path.abspath(os.path.join(os.path.dirname(file_path), new_file_name))

cmds.file(rn=new_save_path)
cmds.file(s=True, f=True,typ="mayaAscii")
