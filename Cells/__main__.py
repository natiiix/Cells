"""This is the main module"""

import time
import constants as const
import Cell
import numpy as np

def get_distance(cell1, cell2):
    """Calculates the distance between two cells."""
    return abs(cell1.position - cell2.position)

# Get the time when the script started executing
START_TIME = time.time()

# Create an empty list for storing cells
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

    # For each cell
    i_src = 0
    while i_src < len(CELLS):
        # Skip cells that are not ready and cells that have already reached the limit mass
        if not CELLS[i_src].ready or CELLS[i_src].mass == const.CELL_MASS_LIMIT:
            i_src += 1
            continue

        target_idx = None
        target_distance = None

        # Find the closest cell with lower mass than the attacking cell
        i_tgt = 0
        while i_tgt < len(CELLS):
            # The attacking cell must have more mass than the target cell
            # in order to be able to successfully attack and it must not attack itself
            if CELLS[i_src].mass > CELLS[i_tgt].mass and i_tgt != i_src:
                # Get the distance between attacking and target cell
                distance = get_distance(CELLS[i_src], CELLS[i_tgt])
                # If the distance to this target cell is lower than the lowest one so far
                if target_idx is None or distance < target_distance:
                    # Update the nearest target information
                    target_idx = i_tgt
                    target_distance = distance

            i_tgt += 1

        # If there is a suitable target cell, perform an attack
        if target_idx is not None:
            # If the attack was successful
            if CELLS[i_src].attack(CELLS[target_idx]):
                # If the mass of the attacking cell exceeds the cell mass limit
                if CELLS[i_src].mass > const.CELL_MASS_LIMIT:
                    # Split the over-the-limit mass from the attacking cell as a new cell
                    CELLS.append(Cell.Cell(
                        CELLS[i_src].position,
                        CELLS[i_src].max_velocity,
                        CELLS[i_src].mass - const.CELL_MASS_LIMIT))

                    # The attacking cell now has the highest possible cell mass
                    CELLS[i_src].mass = const.CELL_MASS_LIMIT

                # Remove the target cell from the list
                CELLS.pop(target_idx)
                # If the target cell had lower index than the
                # attacking one don't increment the iterator
                if target_idx < i_src:
                    continue

        i_src += 1

    # Display the number of living cells for each iteration
    print("[%i] Count: %i" % (i, len(CELLS)))

# Display survivor cells
for cel in CELLS:
    print("Position: %.2f | Velocity: %.3f | Mass: %.3f"
          % (cel.position, cel.max_velocity, cel.mass))

# Execution done, display execution time
print("Done!", time.time() - START_TIME, "seconds")
