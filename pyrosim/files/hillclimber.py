from solution import Solution
import sys
sys.path.insert(0, "../pyrosim")
import pyrosim

class HillClimber:
    def __init__(self):
        self.parent = Solution()
        self.generateBrain()

    def evolve(self):
        self.parent.evaluate()


    def generateWorld(self):
        pyrosim.Start_SDF("df/world.sdf")
        pyrosim.Send_Cube(name=(f"TheWorldCube"), pos = (0, 5, 0.5), size = (1, 1, 1))
        pyrosim.End()


    def generateBody(self):
        pyrosim.Start_URDF("df/body.urdf")
        l, w, h = (1, 1, 1)

        pyrosim.Send_Cube(name=(f"Torso"),
            # pos = (l/2 + l, 0, h/2 + h),    # 1.5, 0, 1.5
            pos = (0, w/2 + w, h/2 + h),
            size = (l, w, h)
        )

        pyrosim.Send_Joint(
            name = "Torso_BackLeg" ,
            parent= "Torso" ,
            child = "BackLeg" ,
            type = "revolute",
            # position = [l, 0, h])
            position = [0, w, h],
            axis = "1 0 0"
        )

        pyrosim.Send_Cube(name=(f"BackLeg"),
            # pos = (-l/2, 0, -h/2),
            pos = (0, -w/2, -h/2),
            size = (l, w, h)
        )

        pyrosim.Send_Joint(
            name = "Torso_FrontLeg" ,
            parent= "Torso" ,
            child = "FrontLeg" ,
            type = "revolute",
            # position = [l/2+l+l/2, 0, h]) # absolute connection to root
            position = [0, w/2 + w + w/2, h],
            axis = "1 0 0"
        )

        pyrosim.Send_Cube(name=(f"FrontLeg"),
            # pos = (l/2, 0, -h/2),    # relative position
            pos = (0, w/2, -h/2),
            size = (l, w, h)
        )

        pyrosim.End()

    def generateBrain(self):
        pyrosim.Start_NeuralNetwork("df/brain.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron( name = 3, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4, jointName = "Torso_FrontLeg")

        for i in range(self.parent.getWeights().shape[0]):
            for j in range(self.parent.getWeights().shape[1]):
                pyrosim.Send_Synapse(
                    sourceNeuronName = i,
                    targetNeuronName = j + 3,
                    weight = self.parent.getWeightAt(i, j),
                )

        pyrosim.End()
