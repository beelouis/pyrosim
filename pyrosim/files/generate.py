import sys
sys.path.insert(0, "../pyrosim/pyrosim")
import pyrosim

pyrosim.Start_SDF("box.sdf")
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])
pyrosim.End()
