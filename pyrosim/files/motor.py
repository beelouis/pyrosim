import numpy as np
import constants as c
import sys
sys.path.insert(0, '..')
import pybullet as p
import pybullet_data
sys.path.insert(0, "../pyrosim")
import pyrosim

class Motor:
    def __init__(self, jointName, robot, i):
        self.jointName = jointName
        self.robot = robot
        self.prepareToAct(i)

    def prepareToAct(self, i):
        if i % 2 == 0:  mod = 1/4
        else:           mod = 1

        self.amplitude  = c.amplitude
        self.frequency  = c.frequency * mod
        self.offset     = c.phaseOffset

        self.inputValues =  self.amplitude * np.sin(np.linspace(
            -np.pi  * self.frequency + self.offset,
            np.pi   * self.frequency + self.offset,
            c.numSteps
            )
        )

    def setValue(self, t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = self.robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.inputValues[t],
            maxForce = 20
        )
