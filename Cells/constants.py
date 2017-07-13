"""This module contains all the constant used by this script."""

# Information regarding initial cells (those created at the start of the script)
# How many cells are supposed to be created
INIT_CELL_COUNT = 1000
# Maximum distance of a cell from the center (position 0.0)
INIT_CELL_POSITION = 100.0
# Highest allowed velocity
INIT_CELL_VELOCITY = 1.0
# Highest allowed initial cell mass
INIT_CELL_MASS = 1.0

# Cell mass at which a cell must split
CELL_MASS_LIMIT = 100.0

# How many iterations (generations of cells) are performed
TARGET_ITERATIONS = 1000
