import numpy as np
import matplotlib.pyplot as plt
import os
import pathlib
import re
import sys

pathAppend = "data"

arg = sys.argv[1]

dir = os.fsencode(f"{pathlib.Path().resolve()}/{pathAppend}")

data = dict()

if arg == "s" or arg == "sensor":
    match_ = False
elif arg == "m" or arg == "motor":
    match_ = True

for file in os.listdir(dir):
    filename = os.fsdecode(file)
    if filename.endswith(".npy"):
        alias = re.split("\.", filename)[0]

        if re.search("_", filename):
            if match_:
                data[alias] = np.load(f"{pathAppend}/{filename}")
        else:
            if not match_:
                data[alias] = np.load(f"{pathAppend}/{filename}")


for i, (dN, dV) in enumerate(data.items()):
    plt.plot(dV, linewidth = 4 - (i*2))

plt.legend([name for name in data.keys()])
plt.show()
