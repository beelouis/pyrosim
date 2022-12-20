import constants as c
from solution import Solution
import copy

class HillClimber:
    def __init__(self):
        self.parent = Solution()

    def evolve(self):
        self.parent.evaluate("G")
        for i, currentGeneration in enumerate(range(c.numGenerations)):
            self.evolveOnce(i)

    def evolveOnce(self, i):
        self.spawn()
        self.mutate()
        self.child.evaluate("D")
        print(f"\n{self.parent.weights}")
        print(f"\n{self.child.weights}")
        print(f"\n================= Generation: {i} =================\n")
        self.select()

    def spawn(self):
        self.child = copy.deepcopy(self.parent)

    def mutate(self):
        self.child.mutate()

    def select(self):
        if self.child.fitness > self.parent.fitness:
            self.parent = self.child

    def showBest(self):
        self.parent.evaluate(arg = "G")
