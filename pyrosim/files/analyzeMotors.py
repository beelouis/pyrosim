import numpy as np
import matplotlib.pyplot as plt

backData = np.load("backMotor.npy")
frontData = np.load("frontMotor.npy")

plt.plot(backData, linewidth = 3)
plt.plot(frontData, linewidth = 1)
plt.legend(["back leg", "front leg"])
plt.show()
