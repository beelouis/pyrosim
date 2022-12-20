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
    def __init__(self, arg):
        self.world = World()
        self.arg = arg

        if self.arg == "G":
            self.physicsClient = p.connect(p.GUI)
        elif self.arg == "D":
            self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.robotID = p.loadURDF("df/body.urdf")

        # p.changeVisualShape(self.robotID, 0, rgbaColor = [1.0, 0.6, 0.5])

        self.planeID = p.loadURDF("plane.urdf")
        #plane comes with pybullet
        p.loadSDF("df/world.sdf")
        p.setGravity(0, 0, -9.8)
        pyrosim.Prepare_To_Simulate(self.robotID)
        self.robot = Robot(self.robotID)

    def run(self):
        for t in range(c.numSteps):
            p.stepSimulation()
            if self.arg == "G":
                time.sleep(c.slp * 100)
            else:
                time.sleep(c.slp)
            self.robot.sense(t)
            self.robot.think()
            self.robot.act()


    def getFitness(self):
        self.robot.getFitness()

    def saveSensorValues(self):
        for sensorName, sensorObj in self.robot.sensors.items():
            np.save(f"{c.pathAppend}/{str(sensorName)}.npy", sensorObj.sValues)

    def __del__(self):
        print("\nbye bye !")
        self.getFitness()
        self.saveSensorValues()
        p.disconnect()
