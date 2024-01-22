# Maya - Pipeline Shelf Tools

## Tool Summary

4 maya shelf tools to automate frequent repetitive tasks. It implements a simple pipeline / 
versioning system to prevent manual file saving / loading / naming, and enforces the 
specified naming convention, and the project directory structure.

## Note

These shelf tools were solely written for specific uses within a personal project. In the future, I will add 
error checking and testing to make it more reliable. But the main logic is there :)

## Setup

To load the custom shelves in Maya, the `shelf_pipeline.mel` script
needs to be included in the directory which contains the start up maya
shelves. The directory usually looks something like this: 
`C:\Users\user\Documents\maya\version\prefs\shelves`. The 
corresponding icons then need to be loaded onto the shelves
inside maya. 


## The Shelf Tools

### Set Project

Custom set project with custom folder names, sets the project
in the specified directory. Also saves current file as version 1 of the specified 
project name. 

### Open Project 

Automates opening the latest version of a specified project in a 
specific topic. 

### Version Up 

Automates saving the current file as the next version while preserving 
previous versions, the naming convention and the folder structure.

### Version Toggle 

Allows toggling between different versions of the current project
file from within maya.