import sys
sys.path.insert(0, "../pyrosim/pyrosim")
import pyrosim


def tower(x, y, z, length, width, height):
    for i in range(10):
        pyrosim.Send_Cube(name=(f"Box{i}"), pos=[x, y, z] , size=[length, width, height])
        z += height
        length *= .9
        width *= .9
        height *=.9

def Create_World(l, w, h, x, y, z):
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name=(f"TheWorldCube"), pos = (x, y+5, z), size = (l, w, h))
    pyrosim.End()

def Create_Robot(l, w, h, x, y, z):
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name=(f"Link0"),
        pos = (x, y, z),    # 0, 0, 0.5
        size = (l, w, h))   # 1, 1, 1

    pyrosim.Send_Joint(
        name = "Link0_Link1" ,
        parent= "Link0" ,
        child = "Link1" ,
        type = "revolute",
        position = [x, y, h]) # 0, 0, 1

    pyrosim.Send_Cube(name=(f"Link1"),
        pos = (0, 0, h/2),    # z = half a cube height above link
        size = (l, w, h))

    pyrosim.Send_Joint(
        name = "Link1_Link2" ,
        parent= "Link1" ,
        child = "Link2" ,
        type = "revolute",
        position = [0, 0, h]) # 0, 0, 1

    pyrosim.Send_Cube(name=(f"Link2"),
        pos = (0, 0, h/2),    # relative positoin
        size = (l, w, h))

    pyrosim.Send_Joint(
        name = "Link2_Link3" ,
        parent= "Link2" ,
        child = "Link3" ,
        type = "revolute",
        position = [0, w/2, h/2]) # 0, 0, 1

    pyrosim.Send_Cube(name=(f"Link3"),
        pos = (0, w/2, 0),    # relative positoin
        size = (l, w, h))

    pyrosim.Send_Joint(
        name = "Link3_Link4" ,
        parent= "Link3" ,
        child = "Link4" ,
        type = "revolute",
        position = [0, w, 0]) # 0, 0, 1

    pyrosim.Send_Cube(name=(f"Link4"),
        pos = (0, w/2, 0),    # relative positoin
        size = (l, w, h))

    pyrosim.Send_Joint(
        name = "Link4_Link5" ,
        parent= "Link4" ,
        child = "Link5" ,
        type = "revolute",
        position = [0, w/2, -h/2]) # 0, 0, 1

    pyrosim.Send_Cube(name=(f"Link5"),
        pos = (0, 0, -h/2),    # relative positoin
        size = (l, w, h))

    pyrosim.Send_Joint(
        name = "Link5_Link6" ,
        parent= "Link5" ,
        child = "Link6" ,
        type = "revolute",
        position = [0, 0, -h]) # 0, 0, 1

    pyrosim.Send_Cube(name=(f"Link6"),
        pos = (0, 0, -h/2),    # relative positoin
        size = (l, w, h))


    pyrosim.End()

size = list([1, 1, 1])
pos = list([0, 0, size[2]/2])

Create_World(size[0], size[1], size[2], pos[0], pos[1], pos[2])
Create_Robot(size[0], size[1], size[2], pos[0], pos[1], pos[2])
