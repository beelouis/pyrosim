import sys
import time
sys.path.insert(0, '..')
import pybullet as p
import pybullet_data
sys.path.insert(0, "../pyrosim/pyrosim")
import pyrosim
import numpy as np
import math

# client handles physics and draws to GUI
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
#plane comes with pybullet
planeID = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

numSteps = 5_00
rightArmSensorValues = np.zeros(numSteps)
leftArmSensorValues = np.zeros(numSteps)
pyrosim.Prepare_To_Simulate(robotID)

for i in range(numSteps):
    p.stepSimulation()
    rightArmSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("RightArm")
    leftArmSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("LeftArm")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotID, # change to robot if this doesnt work
        jointName = b"RightShoulder_RightArm", # change to b"Torso_BackLeg"
        controlMode = p.POSITION_CONTROL,
        targetPosition = math.pi/4.0,
        maxForce = 500
    )

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotID, # change to robot if this doesnt work
        jointName = b"LeftShoulder_LeftArm", # change to b"Torso_BackLeg"
        controlMode = p.POSITION_CONTROL,
        targetPosition = -math.pi/4.0,
        maxForce = 500
    )

    time.sleep(1/60)
    print(i)

np.save("rightArmSensorValues.npy", rightArmSensorValues)
np.save("leftArmSensorValues.npy", leftArmSensorValues)

p.disconnect()
