import constants as c
from solution import Solution
import copy

class ParallelHillClimber:
    def __init__(self):
        self.parents = dict()

        for p in range(c.populationSize):
            self.parents[p] = Solution()

    def evolve(self):
        for parentName, parent in self.parents.items():
            parent.evaluate("G")
            for i, currentGeneration in enumerate(range(c.numGenerations)):
                self.evolveOnce(parentName, parent, i)

    def evolveOnce(self, parentName, parent, i):
        self.spawn(parent)
        self.mutate()
        self.child.evaluate("D")
        print(f"\n{parent.weights}")
        print(f"\n{self.child.weights}")
        print(f"\n======= Parent: {parentName} - Generation: {i+1} =======n")
        self.select(parent)

    def spawn(self, parent):
        self.child = copy.deepcopy(parent)

    def mutate(self):
        self.child.mutate()

    def select(self, parent):
        if self.child.fitness > parent.fitness:
            parent = self.child

    def showBest(self):
        pass
        # self.parent.evaluate(arg = "G")
