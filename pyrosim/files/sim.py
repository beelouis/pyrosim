from simulation import Simulation
import sys

try:
    arg = sys.argv[1]
except IndexError:
    arg = "G"

simulation = Simulation(arg)
simulation.run()
