import constants as c
from solution import Solution
import copy

class HillClimber:
    def __init__(self):
        self.parent = Solution()

    def evolve(self):
        self.parent.evaluate()
        for currentGeneration in range(c.numGenerations):
            self.evolveOnce()

    def evolveOnce(self):
        self.spawn()
        self.mutate()
        self.child.evaluate()
        print(f"\n{self.parent.weights}")
        print(f"\n{self.child.weights}")

        self.select()

    def spawn(self):
        self.child = copy.deepcopy(self.parent)

    def mutate(self):
        self.child.mutate()

    def select(self):
        if self.child.fitness > self.parent.fitness:
            self.parent = self.child
