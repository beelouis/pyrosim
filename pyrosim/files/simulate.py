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

pyrosim.Prepare_To_Simulate(robotID)
backLegSensorValues = np.zeros(numSteps)
frontLegSensorValues = np.zeros(numSteps)


for i in range(numSteps):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    print(i)
    time.sleep(1/60)

np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
np.save("data/backLegSensorValues.npy", backLegSensorValues)

p.disconnect()
