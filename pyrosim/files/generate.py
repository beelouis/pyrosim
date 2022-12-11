import sys
sys.path.insert(0, '../pyrosim')
import pyrosim

sim = pyrosim.Simulator(play_paused=True, eval_time=1000)

sim.start()
sim.wait_to_finish()
