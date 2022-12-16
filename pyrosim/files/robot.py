import sys
from sensor import Sensor
from motor import Motor
import numpy as np
import constants as c
sys.path.insert(0, "../pyrosim")
import pyrosim
from neuralNetwork import NEURAL_NETWORK as NN

class Robot:
    def __init__(self, name):
        self.name = name
        self.nn = NN("df/brain.nndf")
        self.prepareToSense()
        self.prepareToAct()

    def prepareToSense(self):
        self.sensors = dict()
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = Sensor(linkName)

    def sense(self, t):
        for sensor in self.sensors.values():
            sensor.getValue(t)

    def think(self):
        self.nn.Print()

    def prepareToAct(self):
        self.motors = dict()
        for i, jointName in enumerate(pyrosim.jointNamesToIndices):
            # i allows variation of init
            self.motors[jointName] = Motor(jointName, self.name, i)

    def act(self, t):
        for motor in self.motors.values():
            motor.setValue(t)
