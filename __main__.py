"""This is the main module"""

import random

INIT_CELL_COUNT = 100000
TARGET_ITERATIONS = 100000
CELL_SPLIT_LIMIT = 1.0

RAND = random.Random()

cells = []

for i in range(INIT_CELL_COUNT):
    cells.append(RAND.random())

for i in range(TARGET_ITERATIONS):
    attacker = RAND.randrange(0, len(cells))

    defender = attacker
    while defender == attacker:
        defender = RAND.randrange(0, len(cells))

    if cells[attacker] >= cells[defender]:
        cells[attacker] += cells[defender]

        if cells[attacker] >= CELL_SPLIT_LIMIT:
            new_value = cells[attacker] / 2.0
            cells[attacker] = new_value
            cells.append(new_value)

        cells.pop(defender)

    else:
        cells[defender] += cells[attacker]

        if cells[defender] >= CELL_SPLIT_LIMIT:
            new_value = cells[defender] / 2.0
            cells[defender] = new_value
            cells.append(new_value)

        cells.pop(attacker)

    if not i % 100:
        print(i // 100, len(cells), sum(cells))

print("Done!")
