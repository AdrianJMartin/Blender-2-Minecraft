import bpy
from mathutils import *

MC_CUBE_NAME = "mc-cube"

bpy.ops.wm.open_mainfile( filepath="D:\\blender-scripting\\sample-scene.blend" )
D = bpy.data
C = bpy.context


#find the mc-cube object
mc_id = D.objects.find( MC_CUBE_NAME )
mc_object = D.objects[ MC_CUBE_NAME ]

# I think the first data block is the mesh - for mesh obj
mc_mesh = mc_object.data

# I need to know:
#   how to move or set the object position
#   how to get the vertices of the the mesh
#   does moving the object position change the postition
#   of the vertices - or do we need some kind of local
#   to world transform?

mc_object.


if True:
    print("Ok")