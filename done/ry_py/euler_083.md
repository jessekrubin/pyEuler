# Solution to Python problem 83

## Solution code
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Path sum: four ways
Problem 83
NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by moving left, right, up, and down, is indicated in bold red and
is equal to 2297.

          [[131, 673, 234, 103, 18],
           [201,  96, 342, 965, 150],
           [630, 803, 746, 422, 111],
           [537, 699, 497, 121, 956],
           [805, 732, 524,  37, 331]]

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target
As..."), a 31K text file containing a 80 by 80 matrix, from the top left to
the bottom right by moving left, right, up, and down.
"""


def path_sum_four_ways(mat):
    rows = len(mat)  # number of rows
    cols = len(mat[0])  # number of cols
    start = (0, 0)  # starting r and c
    finish = (rows - 1, cols - 1)  # finishing r and c
    visited = set()
    current = {start}
    path_sums = {start: mat[start[0]][start[1]]}

    def adjacents(p):
        r, c = p
        adj = set()
        if r > 0:
            adj.add((r - 1, c))
        if r < rows - 1:
            adj.add((r + 1, c))
        if c > 0:
            adj.add((r, c - 1))
        if c < cols - 1:
            adj.add((r, c + 1))
        return adj

    def iterat(current):
        next = set()
        for point in current:
            for naybor in adjacents(point):
                nval = (mat[naybor[0]][naybor[1]])
                if naybor in path_sums:
                    new = path_sums[point] + nval
                    if path_sums[naybor] > new:
                        path_sums[naybor] = new
                else:
                    path_sums[naybor] = path_sums.get(naybor, nval) + path_sums[point]
                next.add(naybor)
            visited.add(point)
        return next

    for i in range((rows + cols) + 4):
        current = iterat(current)
    return path_sums[finish]


def p083():
    with open('../txt_files/p081_p082_p083_matrix.txt') as f:  # load the matrix
        big_mat = list(list(map(int, row.strip('\n').split(',')))
                       for row in f.readlines())
    return path_sum_four_ways(big_mat)


if __name__ == '__main__':
    lil_mat = [[131, 673, 234, 103, 18],
               [201, 96, 342, 965, 150],
               [630, 803, 746, 422, 111],
               [537, 699, 497, 121, 956],
               [805, 732, 524, 37, 331]]
    assert 2297 == path_sum_four_ways(lil_mat)  # check the small test_pupy case
    answer = p083()
    print("Minimum path FOUR ways: {}".format(answer))
```

## Home made solution dependencies
