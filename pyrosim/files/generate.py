import sys
sys.path.insert(0, "../pyrosim/pyrosim")
import pyrosim

pyrosim.Start_SDF("boxes.sdf")

def tower(x, y, z, length, width, height):
    for i in range(10):
        pyrosim.Send_Cube(name=(f"Box{i}"), pos=[x, y, z] , size=[length, width, height])
        z += height
        length *= .9
        width *= .9
        height *=.9

length, width, height = (.5, .5, .5)
x, y, z = (0, 0, height/2)

for X in range(5):
    for Y in range(5):
        tower(x, y, z, length, width, height)
        y += width
    y = 0
    x += length

pyrosim.End()
