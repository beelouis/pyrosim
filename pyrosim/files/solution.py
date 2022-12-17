import numpy as np

class Solution:
    def __init__(self):
        self.weights = (np.random.rand(3,2) * 2) - 1

    def evaluate(self):
        pass

    def getWeights(self):
        return self.weights

    def getWeightAt(self, i, j):
        return self.weights[i, j]
