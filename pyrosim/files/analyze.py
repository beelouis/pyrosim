import numpy as np
import matplotlib.pyplot as plt

backData = np.load("data/backLegSensorValues.npy")
frontData = np.load("data/frontLegSensorValues.npy")

plt.plot(backData, linewidth = 3)
plt.plot(frontData, linewidth = 1)
plt.legend(["back leg", "front leg"])
plt.show()
