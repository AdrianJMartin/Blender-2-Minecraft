import bpy


import bmesh
from mathutils import *
from mathutils.bvhtree import BVHTree

import json


# bpy.ops.wm.open_mainfile(filepath="D:\\blender-2-minecraft\\sample-scene.blend")
OUTPUTFILE_PATH = "D:\\blender-2-minecraft\\output-data.json"


MC_CUBE_NAME = "mc-cube"

RANGE_LIMIT = 50

D = bpy.data
C = bpy.context

# todo this will eventually be a list of objects to test the cube against.


# I need to know:
#   how to move or set the object position
#   how to get the vertices of the the mesh
#   does moving the object position change the postition
#   of the vertices - or do we need some kind of local
#   to world transform?


# 50 * .6 is 30m x3  in Blender

cubes = []


for z in range(0, RANGE_LIMIT):
    for y in range(0, RANGE_LIMIT):
        for x in range(0, RANGE_LIMIT):

            print("x: ", x, "y: ", y, "z: ", z)

            target_obj = D.objects["Cylinder"]
            target_mesh = target_obj.data
            target_bmesh = bmesh.new()
           
            # find the mc-cube object
            mc_id = D.objects.find(MC_CUBE_NAME)
            mc_object = D.objects[MC_CUBE_NAME]
            # I think the first data block is the mesh - for mesh obj
            mc_mesh = mc_object.data

            mc_object.location.x = x * .6
            mc_object.location.y = y * .6
            mc_object.location.z = z * .6

            layer = bpy.context.view_layer
            layer.update()

            target_bmesh.from_mesh(target_mesh)
            target_bmesh.transform(target_obj.matrix_world)
            target_bvhtree = BVHTree.FromBMesh(target_bmesh)

            mc_bmesh = bmesh.new()
            mc_bmesh.from_mesh(mc_mesh)
            mc_bmesh.transform(mc_object.matrix_world)

            mc_bvhtree = BVHTree.FromBMesh(mc_bmesh)

            intersection_bmesh = mc_bvhtree.overlap(target_bvhtree)

            if intersection_bmesh:
                mat = target_obj.material_slots[0].name
                cubes.append({'x': x, 'y': y, 'z': z, 'mat': mat})

print(cubes)


f = open(OUTPUTFILE_PATH, "w")
f.write(json.dumps(cubes))
f.close()
