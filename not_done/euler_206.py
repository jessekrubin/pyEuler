#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse and Graham Rubin
"""
Concealed Square
Problem 206 
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""


def is_1_2_3_4_5_6_7_8_9_0(n):
    """
    >>> is_1_2_3_4_5_6_7_8_9_0(1122334455667788990)
    True
    >>> is_1_2_3_4_5_6_7_8_9_0(1121314151617181910)
    True
    >>> is_1_2_3_4_5_6_7_8_9_0(11122334455667788990)
    False
    >>> is_1_2_3_4_5_6_7_8_9_0(1112214455667788990)
    False
    """
    # print(n)

    digs = [i for i in str(n)]
    if len(digs) != 19:
        return False
    # print(len(digs))
    ideal = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    inds = (0, 2, 4, 6, 8, 10, 12, 14, 16, 18)
    the_digs = [int(digs[i]) for i in inds]
    # the_digs_strings = (digs[i] for i in inds)
    for i in range(10):
        if ideal[i] != the_digs[i]:
            return False
    return True

    # print(digs)
    # print(the_digs)
    # return the_digs_strings == ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    # return the_digs == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


# upper_bound = 1020304050607080900
# lower_bound = 1929394959697989990


# for i in range(1010101010, 1389026624):
#     if is_1_2_3_4_5_6_7_8_9_0(i**2):
#         print(i)
#         print(i**2)


# print(math.sqrt(upper_bound))
# print(math.sqrt(lower_bound))

# t1 = 1122334455667788990
# t2 = 1121314151617181910
# test1 = (is_1_2_3_4_5_6_7_8_9_0(t1))
# test2 = (is_1_2_3_4_5_6_7_8_9_0(t2))
# print(test1)
# print(test2)

if __name__ == '__main__':
    import doctest

    doctest.testmod()
