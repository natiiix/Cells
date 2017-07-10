"""This is the main module"""

import random

INIT_CELL_COUNT = 100

rand = random.Random()
cells = []

for i in range(INIT_CELL_COUNT):
    cells.append(rand.random())
    print(cells[i])

print(len(cells))
