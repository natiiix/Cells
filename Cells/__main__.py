"""This is the main module"""

import time
import constants as const
import Cell
import numpy as np

def get_distance(cell1, cell2):
    """Calculated the distance between two cells."""
    return abs(cell1.position - cell2.position)

START_TIME = time.time()

CELLS = []

# Generate random initial cells
for _ in range(const.INIT_CELL_COUNT):
    CELLS.append(Cell.Cell(
        np.random.uniform(-const.INIT_CELL_POSITION, const.INIT_CELL_POSITION),
        np.random.uniform(0.0, const.INIT_CELL_VELOCITY),
        np.random.uniform(0.0, const.INIT_CELL_MASS)))

# Perform the evolution for a specified number of iterations
for i in range(const.TARGET_ITERATIONS):
    # New turn, all cells are ready again
    for cel in CELLS:
        cel.ready = True

    i_src = 0
    while i_src < len(CELLS):
        if not CELLS[i_src].ready:
            i_src += 1
            continue

        target_idx = None
        target_distance = None

        i_tgt = 0
        while i_tgt < len(CELLS):
            if CELLS[i_src].mass >= CELLS[i_tgt].mass and i_tgt != i_src:
                distance = get_distance(CELLS[i_src], CELLS[i_tgt])
                if target_idx is None or distance < target_distance:
                    target_idx = i_tgt
                    target_distance = distance

            i_tgt += 1

        if target_idx is not None:
            if CELLS[i_src].attack(CELLS[target_idx]):
                if CELLS[i_src].mass > const.CELL_MASS_LIMIT:
                    CELLS.append(Cell.Cell(
                        CELLS[i_src].position,
                        CELLS[i_src].max_velocity,
                        CELLS[i_src].mass - const.CELL_MASS_LIMIT))

                    CELLS[i_src].mass = const.CELL_MASS_LIMIT

                CELLS.pop(target_idx)
                if target_idx < i_src:
                    continue

        i_src += 1

    print("[%i] Count: %i" % (i, len(CELLS)))

# Display survivor cells
for cel in CELLS:
    print("Position: %.2f | Velocity: %.3f | Mass: %.3f"
          % (cel.position, cel.max_velocity, cel.mass))

print("Done!", time.time() - START_TIME, "seconds")
