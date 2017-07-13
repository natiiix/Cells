"""This module contains definition of the Cell class."""

class Cell:
    """This class stores information about a single cell."""
    position = 0.0
    velocity = 0.0
    mass = 0.0

    def __init__(self, position_init, velocity_init, mass_init):
        self.position = position_init
        self.velocity = velocity_init
        self.mass = mass_init

    def move(self):
        """This method moves the cell as if a single time unit passed."""
        self.position += self.velocity
