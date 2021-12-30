import bpy


import bmesh
from mathutils import *
from mathutils.bvhtree import BVHTree

import json


# bpy.ops.wm.open_mainfile(filepath="D:\\blender-2-minecraft\\sample-scene.blend")
OUTPUTFILE_PATH = "D:\\blender-2-minecraft\\output-data.json"


MC_CUBE_NAME = "mc-cube"

RANGE_LIMIT_X = 32
RANGE_LIMIT_Y = 45
RANGE_LIMIT_Z = 20

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

objsToExport = []

for o in D.objects:
    if o.name.startswith("mc-cube") is False:
        target_obj = D.objects[o.name]
        target_mesh = target_obj.data

        target_bmesh = bmesh.new()
        target_bmesh.from_mesh(target_mesh)
        target_bmesh.transform(target_obj.matrix_world)
        target_bvhtree = BVHTree.FromBMesh(target_bmesh)

        objsToExport.append(
            {'bMesh': target_bvhtree, 'mat': target_obj.material_slots[0].name})

cubes = []

for b in objsToExport:
    for z in range(0, RANGE_LIMIT_Z):
        print(b, z)
        for y in range(0, RANGE_LIMIT_Y):
            for x in range(0, RANGE_LIMIT_X):
                # find the mc-cube object
                mc_id = D.objects.find(MC_CUBE_NAME)
                mc_object = D.objects[MC_CUBE_NAME]
                # I think the first data block is the mesh - for mesh obj
                mc_mesh = mc_object.data

                mc_object.location.x = x 
                mc_object.location.y = y 
                mc_object.location.z = z 

                layer = bpy.context.view_layer
                layer.update()

                mc_bmesh = bmesh.new()
                mc_bmesh.from_mesh(mc_mesh)
                mc_bmesh.transform(mc_object.matrix_world)

                mc_bvhtree = BVHTree.FromBMesh(mc_bmesh)

                intersection_bmesh = mc_bvhtree.overlap(b['bMesh'])

                if intersection_bmesh:

                    # count the number of uniqure cube verts intersecting
                    v = {}
                    for i in intersection_bmesh:
                        v[i[0]] = 1
                    n = len(v)

                    mat = b['mat']
                    cubes.append({'x': x, 'y': y, 'z': z, 'mat': mat,
                                  'overlap': intersection_bmesh is not None, 'vCount': n})
                else:
                    continue

            mc_object.location.x = 0
            mc_object.location.y = 0
            mc_object.location.z = 0


f = open(OUTPUTFILE_PATH, "w")
f.write(json.dumps(cubes))
f.close()
