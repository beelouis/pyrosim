import sys
import time
sys.path.insert(0, '..')
import pybullet as p
import pybullet_data
sys.path.insert(0, "../pyrosim/pyrosim")
import pyrosim
import numpy as np
import random

# client handles physics and draws to GUI
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
#plane comes with pybullet
planeID = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

numSteps = 1_000

pyrosim.Prepare_To_Simulate(robotID)

amplitudeBack = np.pi/4
frequencyBack = 20
phaseOffsetBack = 0

backLegSensorValues = np.zeros(numSteps)
frontLegSensorValues = np.zeros(numSteps)

backLegMotorInput = amplitudeBack * np.sin(np.linspace(
    -np.pi * frequencyBack + phaseOffsetBack,
    np.pi * frequencyBack + phaseOffsetBack,
    numSteps
    )
)

amplitudeFront = np.pi/4
frequencyFront = 10
phaseOffsetFront = np.pi/2

frontLegMotorInput = amplitudeFront * np.sin(np.linspace(
    -np.pi * frequencyFront + phaseOffsetFront,
    np.pi * frequencyFront + phaseOffsetFront,
    numSteps
    )
)

# np.save("backMotor.npy", backLegMotorInput)
# np.save("frontMotor.npy", frontLegMotorInput)
# exit()

for i in range(numSteps):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    if i % 1 == 0:
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotID, # change to robot if this doesnt work
            jointName = b"Torso_BackLeg", # change to b"Torso_BackLeg"
            controlMode = p.POSITION_CONTROL,
            targetPosition = backLegMotorInput[i],
            maxForce = 20
        )

    if i % 1 == 0:
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotID, # change to robot if this doesnt work
            jointName = b"Torso_FrontLeg", # change to b"Torso_BackLeg"
            controlMode = p.POSITION_CONTROL,
            targetPosition = frontLegMotorInput[i],
            maxForce = 20
        )

    print(i)
    time.sleep(1/100)

np.save("frontLegSensorValues.npy", frontLegSensorValues)
np.save("backLegSensorValues.npy", backLegSensorValues)

p.disconnect()
