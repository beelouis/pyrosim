import sys
sys.path.insert(0, '..')
import pyrosim # noqa


sim = pyrosim.Simulator()

class Generic():
    def __init__(self, x, y, z, rx, ry, rz, length, radius):
        self.x = x
        self.y = y
        self.z = z
        self.rx = rx
        self.ry = ry
        self.rz = rz
        self.length = length
        self.radius = radius

    def send(self):
        sim.send_cylinder(
            x = self.x, y = self.y, z = self.z,
            r1 = self.rx, r2 = self.ry, r3 = self.rz,
            length = self.length, radius = self.radius
        )

g = Generic(x = 0.5, y = 0.5, z = 0.5,
            rx = 0, ry = 0, rz = 1, length = 0.3, radius = 0.05)

g.send()


ARM_LENGTH = 0.5
ARM_RADIUS = ARM_LENGTH / 10.0

# sending object returns an ID tag. Use this to later refer to the body
cyl1 = sim.send_cylinder(x=0, y=0, z=ARM_LENGTH / 2.0 + ARM_RADIUS,
                         r1=0, r2=0, r3=1, length=ARM_LENGTH,
                         radius=ARM_RADIUS)

cyl2 = sim.send_cylinder(x=0, y=ARM_LENGTH / 2.0, z=ARM_LENGTH + ARM_RADIUS,
                         r1=0, r2=1, r3=0, length=ARM_LENGTH,
                         radius=ARM_RADIUS)

# when in debug mode, hinge joints are depicted as a red cylinder. This
# is only graphical and does not alter the simulation
sim.send_hinge_joint(first_body_id=cyl1, second_body_id=cyl2,
                     x=0, y=0, z=ARM_LENGTH + ARM_RADIUS,
                     n1=1, n2=0, n3=0, lo=-3.14159 / 4.0, hi=+3.14159 / 4.0)

sim.start()
sim.wait_to_finish()
