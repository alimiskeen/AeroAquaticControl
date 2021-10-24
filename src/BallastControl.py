
class BallastControl:

    def __init__(self, mass: float, center_of_mass: tuple, center_of_buoyancy: tuple):
        # initialize syringe controls
        self.constant_mass = mass
        self.constant_COM = center_of_mass
        self.constant_COB = center_of_buoyancy
