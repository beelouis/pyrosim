import sys
import time
sys.path.insert(0, '..')
import pybullet as p

# client handles physics and draws to GUI
physicsClient = p.connect(p.GUI)

for i in range(1000):
    p.stepSimulation()
    print(i)
    time.sleep(1/60)


p.disconnect()
