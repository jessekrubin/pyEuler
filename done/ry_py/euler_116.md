# Solution to Python problem 116

## Solution code
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Red, green or blue tiles
Problem 116

A row of five black square tiles is to have a number of its tiles replaced
with coloured oblong tiles chosen from red (length two), green (length three),
or blue (length four).

If red tiles are chosen there are exactly seven ways this can be done. If green
tiles are chosen there are three ways. And if blue tiles are chosen there are
two ways.
Assuming that colours cannot be mixed there are 7+3+2 = 12 ways of replacing
the black tiles in a row measuring five units in length.

How many different ways can the black tiles in a row measuring fifty units in
length be replaced if colours cannot be mixed and at least one coloured tile
must be used?

NOTE: This is related to Problem 117.
"""

from pupy.maths import partitions_gen, repermutations


def red_green_or_blue(row_size):
    parts = list(p for p in partitions_gen(row_size, 1, 4)
                 if (len(set(p)) == 2 and 1 in p)
                 or (len((set(p))) == 1 and 1 not in p))
    arrangements = 0
    for part in parts:
        arrangements += repermutations(part)
    return arrangements


def p116():
    return red_green_or_blue(50)



if __name__ == '__main__':
    ANSWER = p116()
    print("# arrangements: {}".format(ANSWER))

```

## Home made solution dependencies
