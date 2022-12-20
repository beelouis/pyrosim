import numpy as np
import random
import os
import sys
sys.path.insert(0, "../pyrosim")
import pyrosim

class Solution:
    def __init__(self):
        self.weights = (np.random.rand(3,2) * 2) - 1

    def evaluate(self, arg):
        self.generateBrain()
        self.generateBody()
        self.generateBrain()
        os.system(f"python sim.py {arg}")
        with open("data/fitness.txt", "r") as fitness:
            self.fitness = float(fitness.read())

    def mutate(self):
        row = random.randint(0, self.weights.shape[0]-1)
        col = random.randint(0, self.weights.shape[1]-1)
        self.weights[row, col] = (random.random()*2) - 1


    def generateWorld(self):
        pyrosim.Start_SDF("df/world.sdf")
        pyrosim.Send_Cube(name=(f"TheWorldCube"), pos = (0, 5, 0.5), size = (1, 1, 1))
        pyrosim.End()


    def generateBody(self):
        pyrosim.Start_URDF("df/body.urdf")
        l, w, h = (1, 1, 1)

        pyrosim.Send_Cube(
            name=(f"Torso"),
            pos = (0, w/2 + w, h/2 + h),
            size = (l, w, h)
        )
        pyrosim.Send_Joint(
            name = "Torso_BackLeg" ,
            parent= "Torso" ,
            child = "BackLeg" ,
            type = "revolute",
            position = [0, w, h],
            axis = "1 0 0"
        )
        pyrosim.Send_Cube(
            name=(f"BackLeg"),
            pos = (0, -w/2, -h/2),
            size = (l, w, h)
        )
        pyrosim.Send_Joint(
            name = "Torso_FrontLeg" ,
            parent= "Torso" ,
            child = "FrontLeg" ,
            type = "revolute",
            position = [0, w/2 + w + w/2, h],
            axis = "1 0 0"
        )
        pyrosim.Send_Cube(
            name=(f"FrontLeg"),
            pos = (0, w/2, -h/2),
            size = (l, w, h)
        )
        pyrosim.End()

    def generateBrain(self):
        pyrosim.Start_NeuralNetwork("df/brain.nndf")
        
        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron(name = 3, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_FrontLeg")

        for i in range(self.weights.shape[0]):
            for j in range(self.weights.shape[1]):
                pyrosim.Send_Synapse(
                    sourceNeuronName = i,
                    targetNeuronName = j + 3,
                    weight = self.weights[i, j],
                )

        pyrosim.End()
