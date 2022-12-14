import sys
import time
sys.path.insert(0, '..')
import pybullet as p
import pybullet_data
sys.path.insert(0, "../pyrosim/pyrosim")
import pyrosim
import numpy as np

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

    time.sleep(1/60)
    print(i)

np.save("rightArmSensorValues.npy", rightArmSensorValues)
np.save("leftArmSensorValues.npy", leftArmSensorValues)

p.disconnect()
