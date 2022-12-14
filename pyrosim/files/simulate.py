import sys
import time
sys.path.insert(0, '..')
import pybullet as p
import pybullet_data
sys.path.insert(0, "../pyrosim/pyrosim")
import pyrosim
import numpy as np
import math
import random

# client handles physics and draws to GUI
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
#plane comes with pybullet
planeID = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

numSteps = 1000

pyrosim.Prepare_To_Simulate(robotID)
backLegSensorValues = np.zeros(numSteps)
frontLegSensorValues = np.zeros(numSteps)


for i in range(numSteps):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    if i % 20 == 0:
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotID, # change to robot if this doesnt work
            jointName = b"Torso_BackLeg", # change to b"Torso_BackLeg"
            controlMode = p.POSITION_CONTROL,
            targetPosition = (random.random() * math.pi/2) - math.pi/4,
            maxForce = 20
        )

        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotID, # change to robot if this doesnt work
            jointName = b"Torso_FrontLeg", # change to b"Torso_BackLeg"
            controlMode = p.POSITION_CONTROL,
            targetPosition = (random.random() * math.pi/2) - math.pi/4,
            maxForce = 20
        )

    print(i)
    time.sleep(1/60)

np.save("frontLegSensorValues.npy", frontLegSensorValues)
np.save("backLegSensorValues.npy", backLegSensorValues)

p.disconnect()
