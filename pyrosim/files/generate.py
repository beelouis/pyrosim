import sys
sys.path.insert(0, "../pyrosim/pyrosim")
import pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(
        name=(f"TheWorldCube"),
        pos = (0, 5, 0.5),
        size = (1, 1, 1)
    )
    pyrosim.End()

def Create_Robot():
    # body size and position: absolute
    bodyL, bodyW, bodyH = (1, 1, 1)
    bodyX, bodyY, bodyZ = (0, 0, bodyH/2)

    # right shoulder joint position (absolute)
    rsjX, rsjY, rsjZ = (bodyL/2, 0, bodyH)
    # right shoulder position and size (relative to joint^)
    rsL, rsW, rsH = (0.1, 0.1, 0.1)
    rsX, rsY, rsZ = (rsL/2, 0, 0)

    # left shoulder joint position (absolute)
    lsjX, lsjY, lsjZ = (-bodyL/2, 0, bodyH)
    # left shoulder position and size (relative to joint^)
    lsL, lsW, lsH = (0.1, 0.1, 0.1)
    lsX, lsY, lsZ = (-lsL/2, 0, 0)

    # both arms are the same size
    armL, armW, armH = (1, 0.25, 0.25)

    # joint: right shoulder to right arm (relative)
    rajX, rajY, rajZ = (rsL, 0, 0)
    # position of right arm relative to joint^
    rightArmX, rightArmY, rightArmZ = (bodyL/2, 0, 0)

    # joint: left shoulder to left arm (relative)
    lajX, lajY, lajZ = (-lsL, 0, 0)
    # position of left arm relative to joint^
    leftArmX, leftArmY, leftArmZ = (-bodyL/2, 0, 0)


    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name=(f"Torso"),
        pos = (bodyX, bodyY, bodyZ),
        size = (bodyL, bodyW, bodyH) # abs
    )

    pyrosim.Send_Joint(
        name = "Torso_RightShoulder" ,
        parent= "Torso" ,
        child = "RightShoulder" ,
        type = "revolute",
        position = [rsjX, rsjY, rsjZ] # abs
    )

    pyrosim.Send_Cube(name=(f"RightShoulder"),
        pos = (rsX, rsY, rsZ),
        size = (rsL, rsW, rsH)
    )

    pyrosim.Send_Joint(
        name = "RightShoulder_RightArm" ,
        parent= "RightShoulder" ,
        child = "RightArm" ,
        type = "revolute",
        position = [rajX, rajY, rajZ],
        axis = "0 0 1"
    )

    pyrosim.Send_Cube(name=(f"RightArm"),
        pos = (rightArmX, rightArmY, rightArmZ),
        size = (armL, armW, armH)
    )

    pyrosim.Send_Joint(
        name = "Torso_LeftShoulder" ,
        parent= "Torso" ,
        child = "LeftShoulder" ,
        type = "revolute",
        position = [lsjX, lsjY, lsjZ]
    )

    pyrosim.Send_Cube(name=(f"LeftShoulder"),
        pos = (lsX, lsY, lsZ),
        size = (lsL, lsW, lsH)
    )

    pyrosim.Send_Joint(
        name = "LeftShoulder_LeftArm",
        parent= "LeftShoulder" ,
        child = "LeftArm" ,
        type = "revolute",
        position = [lajX, lajY, lajZ],
        axis = "0 0 1"
    )

    pyrosim.Send_Cube(name=(f"LeftArm"),
        pos = (leftArmX, leftArmY, leftArmZ),
        size = (armL, armW, armH)
    )


    pyrosim.End()


Create_World()
Create_Robot()
