#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse Rubin ~ project Euler ~
"""
First Sort II
http://projecteuler.net/problem=524
Consider the following algorithm for sorting a list:
1. Starting from the beginning of the list, check each pair of adjacent elements in turn.
2. If the elements are out of order:
a. Move the smallest element of the pair at the beginning of the list.
b. Restart the process from step 1.
3. If all pairs are in order, stop.For example, the list  4 1 3 2  is sorted as follows:
4 1 3 2  (4 and 1 are out of order so move 1 to the front of the list)
1 4 3 2  (4 and 3 are out of order so move 3 to the front of the list)
3 1 4 2  (3 and 1 are out of order so move 1 to the front of the list)
1 3 4 2  (4 and 2 are out of order so move 2 to the front of the list)
2 1 3 4  (2 and 1 are out of order so move 1 to the front of the list)
1 2 3 4  (The list is now sorted)Let F(L) be the number of times step 2a is executed to sort list L. For example, F( 4 1 3 2 ) = 5.
We can list all permutations P of the integers 1, 2, ..., n in lexicographical order, and assign to each permutation an index In(P) from 1 to n! corresponding to its position in the list.
Let Q(n, k) = min(In(P)) for F(P) = k, the index of the first permutation requiring exactly k steps to sort with First Sort. If there is no permutation for which F(P) = k, then Q(n, k) is undefined.
For n = 4 we have:
PI4(P)F(P)1, 2, 3, 410Q(4, 0) = 11, 2, 4, 324Q(4, 4) = 21, 3, 2, 432Q(4, 2) = 31, 3, 4, 2421, 4, 2, 356Q(4, 6) = 51, 4, 3, 2642, 1, 3, 471Q(4, 1) = 72, 1, 4, 385Q(4, 5) = 82, 3, 1, 4912, 3, 4, 11012, 4, 1, 31152, 4, 3, 1123Q(4, 3) = 123, 1, 2, 41333, 1, 4, 21433, 2, 1, 41523, 2, 4, 11623, 4, 1, 21733, 4, 2, 11824, 1, 2, 3197Q(4, 7) = 194, 1, 3, 22054, 2, 1, 32164, 2, 3, 12244, 3, 1, 22344, 3, 2, 1243Let R(k) = min(Q(n, k)) over all n for which Q(n, k) is defined.
Find R(1212).
"""

def p524():
    pass

if __name__ == '__main__':
    p524()