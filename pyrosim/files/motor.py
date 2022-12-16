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

    def setValue(self, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = self.robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 20
        )
