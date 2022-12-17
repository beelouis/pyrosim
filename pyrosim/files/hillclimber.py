from solution import Solution

class HillClimber:
    def __init__(self):
        self.parent = Solution()

    def evolve(self):
        self.parent.evaluate()
