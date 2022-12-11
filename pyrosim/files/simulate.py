import sys
import time
sys.path.insert(0, '..')
import pybullet as p
import pybullet_data

# client handles physics and draws to GUI
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
#plane comes with pybullet
planeID = p.loadURDF("plane.urdf")
p.loadSDF("boxes.sdf")

for i in range(1000):
    p.stepSimulation()
    print(i)
    time.sleep(1/60)


p.disconnect()
