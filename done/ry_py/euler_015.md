# Solution to Python problem 15

## Solution code
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""


def calc_next_row(row):
    row_size = len(row)
    next_row = [0] * row_size
    for i in range(row_size):
        if i == 0:
            next_row[i] = 1
        else:
            next_row[i] += row[i] + next_row[i - 1]
    return next_row


def p015():
    size = 20 + 1
    grid = []
    first_row = [1, ] * size
    grid.append(first_row)
    while len(grid) < 21: grid.append(calc_next_row(grid[-1]))
    return grid[-1][-1]


if __name__ == '__main__':
    ANSWER = p015()
    print("There are {} routes on a a 20x20 grid".format(ANSWER))

```

## Home made solution dependencies
