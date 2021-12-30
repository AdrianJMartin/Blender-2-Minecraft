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

for b in data:
    output.write("Send /\n")
    output.write("Send fill ~%d ~%d ~%d ~%d ~%d ~%d %s\n" % (
        b['x'] * -1, b['z'], b['y'],
        b['x'] * -1, b['z'], b['y'],
        b['mat']))
    output.write("Send {Return}\n")
    output.write("\n")


footer = open("output-template-footer.txt", encoding="utf8")
output.write(footer.read())
footer.close()


output.close()
