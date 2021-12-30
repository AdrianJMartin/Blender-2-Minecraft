# Blender 2 Minecraft - ( via AHK )
## Steps

* Load the sample scene
* Prepare you objects in xyz +ve octant - Make the looping easier
* Name the object's first material after the Minecraft block name.
* Run the script
* Blender should output an itermediate output-data.json file
* We then need to move to a python enviroment - I'm using VSCode etc.
* Run the output-to-ahk.py script - this should generate output.ahk file.
* Start Minecraft, position your guy where you want the Blender 0,0,0 to be. The scene will always be in MC's xyz orienatation.
* Go into Creative Mode. Position you guy. and put MC into pause mode(esc)
* launch the output.ahk script 

    ```powershell
        > ./output.ahk
    ```
* 

# Todo
* DONE! Convert it to generate strips of blocks, this should be many times quicker.
* Add a small offset to the coords to make sure that blocks are not created on the same space as the guy. As this will push the guy to another position and change the relative coords.
* Profit?
* Multiple objects in the Blender Scene
* take range limits from scene



## Rough Notes

Simple program to convert Blender models to minecraft blocks

Initial plan is to move a cube through x,y,z and if the cube touches/intersects then add it.

Some how use talk/console and /fill maybe /clone - AutoHotKey or just use SendMsg direct

blender material name to block type

# Python Environment Setup
Sort of from here:

https://b3d.interplanety.org/en/using-microsoft-visual-studio-code-as-external-ide-for-writing-blender-scripts-add-ons/

# Dev Problems
The Blender VSCode extension throws a EXCEPTION_ACCESS_VIOLATION when trying to update the view_layer. - Copying the script to the .blend stops the issue, but we lose the debugger 😥





