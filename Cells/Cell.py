"""This module contains definition of the Cell class."""

class Cell:
    """This class stores information about a single cell."""

    def __init__(self, position_init, max_velocity_init, mass_init):
        self.position = position_init
        self.max_velocity = max_velocity_init
        self.mass = mass_init
        self.ready = False

    def attack(self, target):
        """This method moves this cell as close to another cell as possible
        and eats the target cell if its within this cell's reach."""
        # Calculate position difference between the cells
        pos_diff = target.position - self.position

        self.ready = False

        # The distance is lower than the Cell's velocity
        if abs(pos_diff) < self.max_velocity:
            self.position += pos_diff
            self.mass += target.mass
            return True
        # The distance is higher and the position is higher
        elif pos_diff > 0.0:
            self.position += self.max_velocity
            return False
        # The distance is higher and the position is lower
        else:
            self.position -= self.max_velocity
            return False
