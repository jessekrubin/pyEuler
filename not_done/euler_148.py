#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Problem 0
template
"""
from tqdm import tqdm


def next_pascal_row(row):
    len_next_row = len(row)
    retrow = [1] * len_next_row  # like scooby doo
    for i in range(1, len(row), 1):
        retrow[i] = row[i] + row[i - 1]
    return retrow + [1]


def pascal_triangle_divisible_by_7(num_rows):
    upper_bound_49 = int(num_rows/49) + 1
    sevens = {49*i for i in range(1, upper_bound_49)}
    print(sevens)
    not_divsible_by_seven = 0
    num_entries = 0
    rowrowrow = [1]
    print("starting")
    inc = 1
    mul = 1
    cur = 1
    tot = 0
    nd = 0
    for i in range(1, num_rows+1):
        n_div7 = sum((1 for j in rowrowrow if j % 7 != 0))

        not_divsible_by_seven += n_div7
        # print(sum((1 for j in rowrowrow if j % 7 == 0)))
        num_entries += len(rowrowrow)
        rowrowrow = next_pascal_row(rowrowrow)

        tot += i
        nd += cur

        print("____")
        print(i, n_div7, cur)

        if i% 49 == 0:
            # inc = 1
            mul += 1
            # cur = inc * mul
            inc = mul
            cur = inc
        elif i%7 == 0:
            inc += mul
            cur = inc
        else:
            cur += inc
    # print(rowrowrow)
    print("")
    print(not_divsible_by_seven)
    print(num_entries)
    print("")
    print(nd)
    print(tot)

def p148(num_rows):
    inc = 1
    mul = 1
    cur = 1
    tot = 0
    nd = 0
    for i in tqdm(range(1, num_rows+1), total=num_rows):
        tot += i
        nd += cur
        if i % 49 == 0:
            # inc = 1
            mul += 1
            # cur = inc * mul
            inc = 1*mul
            cur = inc
        elif i%7 == 0:
            inc += 1*mul
            cur = inc
        else:
            cur += inc
    return tot, nd

pascal_triangle_divisible_by_7(7)
pascal_triangle_divisible_by_7(1000)

# total_entries, not_div_seven = p148(100)
# print(total_entries, not_div_seven)
# total_entries, not_div_seven = p148(10**9)
# print(total_entries, not_div_seven)
