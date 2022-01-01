# this script will only export objects named block_*

import bpy
from bpy.types import SceneObjects

import os


print("Start")

D = bpy.data
C = bpy.context

outputDir = os.path.dirname(D.filepath)
outputPath = os.path.join(outputDir, "output-blocks.ahk")

output = open(outputPath, "w", encoding="utf8")

headerPath = os.path.join(outputDir, "output-template-header.txt")
header = open(headerPath, encoding="utf8")
output.write(header.read())
header.close()


for o in D.scenes[0].objects:

    if o.name.startswith("block_"):

        if o.scale.x != 1:
            print("Warning %s x scale is not set to 1" % (o.name))
        if o.scale.y != 1:
            print("Warning %s y scale is not set to 1" % (o.name))
        if o.scale.z != 1:
            print("Warning %s z scale is not set to 1" % (o.name))

        if o.rotation_euler.x != 0:
            print("Warning %s x rotation is not set to 0" % (o.name))
        if o.rotation_euler.y != 0:
            print("Warning %s y rotation is not set to 0" % (o.name))
        if o.rotation_euler.z != 0:
            print("Warning %s z rotation is not set to 0" % (o.name))

        mesh = o.data

        x1 = y1 = z1 = 1000
        for v in mesh.vertices:
            if v.co.x < x1:
                x1 = round(v.co.x)
            if v.co.y < y1:
                y1 = round(v.co.y)
            if v.co.z < z1:
                z1 = round(v.co.z)

        x2 = y2 = z2 = -1000
        for v in mesh.vertices:
            if v.co.x > x2:
                x2 = round(v.co.x)
            if v.co.y > y2:
                y2 = round(v.co.y)
            if v.co.z > z2:
                z2 = round(v.co.z)

        xw = x2 - x1
        yw = y2 - y1
        zw = z2 - z1

        if xw % 1 != 0:
            print("Warning %s is not aligned to the grid!" % (o.name))
        if yw % 1 != 0:
            print("Warning %s is not aligned to the grid!" % (o.name))
        if zw % 1 != 0:
            print("Warning %s is not aligned to the grid!" % (o.name))

        if xw == 0:
            print("Warning %s has 0 x size!" % (o.name))
        if yw == 0:
            print("Warning %s has 0 y size!" % (o.name))
        if zw == 0:
            print("Warning %s has 0 z size!" % (o.name))

        m = o.material_slots[0].name

        output.write("Send /\n")
        output.write("Clipboard := \"fill ~%d ~%d ~%d ~%d ~%d ~%d %s\"\n" % (x1 * -1, z1, y1, x2 * -1, z2, y2, m))
        output.write("Send ^v\n")
        output.write("Send {Return}\n")
        output.write("\n")

footerPath = os.path.join(outputDir, "output-template-footer.txt")
header = open(footerPath, encoding="utf8")
output.write(header.read())
header.close()


print("Finish")
