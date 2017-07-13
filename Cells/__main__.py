"""This is the main module"""

import numpy as np
import time

start_time = time.time()

INIT_CELL_COUNT = 100000
TARGET_ITERATIONS = 100000
CELL_SPLIT_LIMIT = 1.0

CELLS = list(np.random.uniform(0.0, 1.0, INIT_CELL_COUNT))

for i in range(INIT_CELL_COUNT):
    CELLS.append(np.random.rand())

for i in range(TARGET_ITERATIONS):
    attacker = np.random.randint(0, len(CELLS))

    defender = attacker
    while defender == attacker:
        defender = np.random.randint(0, len(CELLS))

    if CELLS[attacker] >= CELLS[defender]:
        CELLS[attacker] += CELLS[defender]

        if CELLS[attacker] >= CELL_SPLIT_LIMIT:
            new_value = CELLS[attacker] / 2.0
            CELLS[attacker] = new_value
            CELLS.append(new_value)

        CELLS.pop(defender)

    else:
        CELLS[defender] += CELLS[attacker]

        if CELLS[defender] >= CELL_SPLIT_LIMIT:
            new_value = CELLS[defender] / 2.0
            CELLS[defender] = new_value
            CELLS.append(new_value)

        CELLS.pop(attacker)

    if not i % 1000:
        print(i, len(CELLS), sum(CELLS))

print("Done!", time.time() - start_time, "seconds")
