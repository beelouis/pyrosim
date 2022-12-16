import sys
import time
import constants as c
from world import World
from robot import Robot
import numpy as np
sys.path.insert(0, '..')
import pybullet as p
import pybullet_data

sys.path.insert(0, "../pyrosim")
import pyrosim

class Simulation:
    def __init__(self):
        self.world = World()

        self.physicsClient = p.connect(p.GUI)
        # client handles physics and draws to GUI
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.robotID = p.loadURDF("df/body.urdf")
        self.planeID = p.loadURDF("plane.urdf")
        #plane comes with pybullet
        p.loadSDF("df/world.sdf")
        p.setGravity(0, 0, -9.8)
        pyrosim.Prepare_To_Simulate(self.robotID)
        self.robot = Robot(self.robotID)

    def run(self):
        for t in range(c.numSteps):
            p.stepSimulation()
            time.sleep(c.slp)
            self.robot.sense(t)
            self.robot.think()
            self.robot.act()

    def saveSensorValues(self):
        for sensorName, sensorObj in self.robot.sensors.items():
            np.save(f"{c.pathAppend}/{str(sensorName)}.npy", sensorObj.sValues)

    def saveMotorValues(self):
        for motorName, motorObj in self.robot.motors.items():
            np.save(f"{c.pathAppend}/{str(motorName)[2:-1]}.npy", motorObj.inputValues)

    def __del__(self):
        print("bye bye !")
        self.saveSensorValues()
        self.saveMotorValues()
        p.disconnect()
