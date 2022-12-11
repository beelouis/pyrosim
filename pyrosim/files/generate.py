import sys
sys.path.insert(0, "../pyrosim/pyrosim")
import pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name=(f"TheWorldCube"), pos = (0, 5, 0.5), size = (1, 1, 1))
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    l, w, h = (1, 1, 1)

    pyrosim.Send_Cube(name=(f"Torso"),
        pos = (l/2 + l, 0, h/2 + h),    # 1.5, 0, 1.5
        size = (l, w, h))

    pyrosim.Send_Joint(
        name = "Torso_BackLeg" ,
        parent= "Torso" ,
        child = "BackLeg" ,
        type = "revolute",
        position = [l, 0, h])

    pyrosim.Send_Cube(name=(f"BackLeg"),
        pos = (-l/2, 0, -h/2),
        size = (l, w, h))

    pyrosim.Send_Joint(
        name = "Torso_FrontLeg" ,
        parent= "Torso" ,
        child = "FrontLeg" ,
        type = "revolute",
        position = [l/2+l+l/2, 0, h]) # absolute connection to root

    pyrosim.Send_Cube(name=(f"FrontLeg"),
        pos = (l/2, 0, -h/2),    # relative position
        size = (l, w, h))



    pyrosim.End()


Create_World()
Create_Robot()
