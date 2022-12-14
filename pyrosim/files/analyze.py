import numpy as np
import matplotlib.pyplot as plt

right = np.load("rightArmSensorValues.npy")
left = np.load("leftArmSensorValues.npy")

plt.plot(right, linewidth = 3)
plt.plot(left, linewidth = 1)
plt.legend(["Left Arm", "Right Arm"])
plt.show()
