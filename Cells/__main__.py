"""This is the main module"""

import time
import constants as const
import Cell
import numpy as np

def main():
    """The main function of the script."""
    cells = []

    for _ in range(const.INIT_CELL_COUNT):
        cells.append(Cell.Cell(
            np.random.uniform(-const.INIT_CELL_POSITION, const.INIT_CELL_POSITION),
            np.random.uniform(-const.INIT_CELL_VELOCITY, const.INIT_CELL_VELOCITY),
            np.random.uniform(-const.INIT_CELL_MASS, const.INIT_CELL_MASS)))

    for i in range(const.TARGET_ITERATIONS):
        max_pos = 0.0
        min_pos = 0.0

        for cel in cells:
            cel.move()

            if cel.position > max_pos:
                max_pos = cel.position

            if cel.position < min_pos:
                min_pos = cel.position

        print("[%i] Max: %f | Min: %f" % (i, max_pos, min_pos))

START_TIME = time.time()

main()

print("Done!", time.time() - START_TIME, "seconds")
