#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Problem 0
template
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Problem 0
template
"""


def pascal_div_seven(n):
    nent = sum(i for i in range(1, n + 1))
    ret_sum = 0
    loop_number = 1
    cur_thing = 6
    for loop in range(1, n + 1):
        print(cur_thing)
        ret_sum += cur_thing
        if cur_thing == 0:
            loop_number += 1
            cur_thing = 6 * loop_number

else:
cur_thing -= loop_number
print(loop_number)
print(nent)
print(ret_sum)
print((nent - ret_sum))
return ret_sum

answer = pascal_div_seven(21)
print(answer)


def next_pascal_row(row):
    len_next_row = len(row)
    retrow = [1] * len_next_row  # like scooby doo
    for i in range(1, len(row), 1):
        retrow[i] = row[i] + row[i - 1]
    return retrow + [1]


def pascal_triangle_divisible_by_7(num_rows):
    not_divsible_by_seven = 0
    num_entries = 0
    rowrowrow = [1]
    print("starting")
    for i in range(num_rows):
        not_divsible_by_seven += sum((1 for j in rowrowrow if j % 7 != 0))
        print(sum((1 for j in rowrowrow if j % 7 == 0)))
        num_entries += len(rowrowrow)
        rowrowrow = next_pascal_row(rowrowrow)
    print(rowrowrow)
    print(not_divsible_by_seven)
    print(num_entries)


pascal_triangle_divisible_by_7(7)
pascal_triangle_divisible_by_7(100)
#
# def solution_thingy(n_rows):
#     numgoaroudns= n_rows - 7
#     loopnum = 2
#     cur_number = 6
#     totoal = 0
#     for i in range(numgoaroudns):
#         # print(cur_number)
#         totoal += cur_number
#         cur_number -= 2
#     print(totoal)


solution_thingy(100)

# pascal_triangle_divisible_by_7(1000000000)
