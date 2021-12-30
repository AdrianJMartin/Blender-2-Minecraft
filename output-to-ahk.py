import json

data = json.load(open("output-data.json", encoding="utf8"))

# input from blender
# x +ve to the right
# y +ve forward
# z +ve up


# output minecraft
#  x seems to be postive to the left -ve to the right
#  y up +ve
#  z forward +ve

# x -> *1 -> x
# y -> z
# z -> y


output = open("output.ahk", "w", encoding="utf8")

header = open("output-template-header.txt", encoding="utf8")

output.write(header.read())
header.close()

beginStrip = True
maxIndex = len(data) - 1

i = -1

newStrip = True

while True:
    i = i + 1

    if i > len(data):
        break

    if newStrip:
        b = data[i]
        newStrip = False
        x1 = b['x'] * -1
        y1 = b['z']
        z1 = b['y']
        mat1 = b['mat']

        output.write("Send /\n")
        output.write("Clipboard := \"fill ~%d ~%d ~%d " % (x1, y1, z1))

    if i < len(data) - 1:
        b = data[i + 1]
        x2 = b['x'] * -1
        y2 = b['z']
        z2 = b['y']
        mat2 = b['mat']
    else:
        output.write("~%d ~%d ~%d %s\"\n" % (x, y, z, mat1))
        output.write("Send ^v\n")
        output.write("Send {Return}\n")
        output.write("\n")
        break

    # are they in the same strip?
    if y1 == y2 and z1 == z2:
        x = x2
        y = y2
        z = z2
        continue
    else:
        output.write("~%d ~%d ~%d %s\"\n" % (x, y, z, mat1))
        output.write("Send ^v\n")
        output.write("Send {Return}\n")
        output.write("\n")
        newStrip = True

footer = open("output-template-footer.txt", encoding="utf8")
output.write(footer.read())
footer.close()
output.close()
