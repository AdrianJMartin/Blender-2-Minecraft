# Blender 2 Minecraft - ( via AHK )
## Pre Req
* Minecraft - I used Java Edition - it might work with Bedrock...
* Python 3.x - I've matched versions with the one used in the current version of Blender, Python 3.9.7
* Blender 3d - Current release 3.0

## Steps

* Load the sample scene
* Prepare you objects in xyz +ve octant - This makes the looping easier
* Name the object's first material after the Minecraft block name.
* Run the script
* Blender should output an itermediate output-data.json file
* We then need to move to a python enviroment - I'm using VSCode etc.
* Run the output-to-ahk.py script - this should generate output.ahk file.
* Start Minecraft and go into a Creative mode world. Position Steve. and put MC into pause mode(esc), the building will always be in MC's xyz orienatation. DONT move Steve! it will upset the relative coords, Also make sure your Blender scene is not going to push Steve arround.
* launch the output.ahk script 

    ```powershell
        > ./output.ahk
    ```

# Todo
* DONE! Convert it to generate strips of blocks, this should be many times quicker.
* Be extension of above - break it down to largest cubes, would make it again many times quicker.
* Add a small offset to the coords to make sure that blocks are not created on the same space as Steve, As this will push Steve to another position and change the relative coords.
* Profit?
* Multiple objects in the Blender Scene - first draft done...not bad..but thinking that this should be a tool that makes building easier rather than a straight export anything to MC. ie Work with the Blender grid....stick to convex hulls...
* Take range limits from scene
* Create a pre-run script - that shows orientation in mc world. Say a simple axis model.
* Create a post run delete script? - file a->b with air!

## Notes
### 31 Dec 2021
* I'm coming to the conclusion that I need to use a model of some sort to process the data rather than parsing a list of blocks
    * so...some kind of in memory model or simple DB...SQLLite.
* If a mesh only has 8 vertices then we could assume its a cubiod and use block fill.
   




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





