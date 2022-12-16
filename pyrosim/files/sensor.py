import constants as c
import numpy as np
import sys
sys.path.insert(0, "../pyrosim")
import pyrosim

class Sensor:
    def __init__(self, linkName):
        self.linkName = linkName
        self.prepareToSense()

    def prepareToSense(self):
        self.sValues = np.zeros(c.numSteps)

    def getValue(self, t):
        self.sValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
