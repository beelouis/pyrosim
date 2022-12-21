import sys
from sensor import Sensor
from motor import Motor
import numpy as np
import constants as c
import pybullet as p
sys.path.insert(0, "../pyrosim")
import pyrosim
from neuralNetwork import NEURAL_NETWORK as NN

class Robot:
    def __init__(self, id):
        self.id = id
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
        self.nn.Update()

    def prepareToAct(self):
        self.motors = dict()
        for i, jointName in enumerate(pyrosim.jointNamesToIndices):
            self.motors[jointName] = Motor(jointName, self.id, i)

    def act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)

                for motor in self.motors.values():
                    if str(motor.jointName)[2:-1] == jointName:
                        motor.setValue(desiredAngle)

    def getFitness(self):
        stateLink0 = p.getLinkState(self.id, 0)
        posLink0 = stateLink0[0]
        yLink0 = posLink0[1]
        with open("data/fitness.txt", "w") as fitness:
            fitness.write(str(yLink0))
