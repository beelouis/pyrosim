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
robotID = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

for i in range(3000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)


p.disconnect()
