# coding=utf-8

"""
Dice Game
Problem 205
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins.
The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer
rounded to seven decimal places in the form 0.abcdefg
"""
from itertools import combinations, permutations, combinations_with_replacement


from tqdm import tqdm
from collections import defaultdict

for c in combinations_with_replacement('1234', 4):
    print(c)
    for ccc in permutations(c):
        print(ccc)

# def dice(n_dice, n_sides):
#     n_four_dice = n_dice
#     four_side = [i + 1 for i in range(n_sides)]*n_dice
#     vals = {}
#     tot = n_sides** n_dice
#     print(tot)
#     for combo in tqdm(combinations(four_side, n_four_dice),total=tot):
#         # print(combo)
#         try:
#             vals[sum(combo)] += 1
#         except:
#             vals[sum(combo)] = 1
#     return vals

from tqdm import tqdm
from collections import defaultdict

for c in combinations_with_replacement('1234', 4):
    print(c)
    for ccc in permutations(c):
        print(ccc)

# def dice(n_dice, n_sides):
#     n_four_dice = n_dice
#     four_side = [i + 1 for i in range(n_sides)]*n_dice
#     vals = {}
#     tot = n_sides** n_dice
#     print(tot)
#     for combo in tqdm(combinations(four_side, n_four_dice),total=tot):
#         # print(combo)
#         try:
#             vals[sum(combo)] += 1
#         except:
#             vals[sum(combo)] = 1
#     return vals


# peter = dice(9, 4)
# print(peter)
# peter = {21: 11096964, 22: 12352824, 23: 12352824,
#          24: 11096964, 19: 6428241, 20: 8928225, 18: 4106737,
#          25: 8928225, 17: 2315709, 16: 1137564, 26: 6428241,
#          27: 4106737, 15: 478080, 28: 2315709, 29: 1137564, 30: 478080,
#          14: 168480, 13: 47304, 12: 10053, 31: 168480, 11: 1377,
#          10: 81, 32: 47304, 33: 10053, 9: 1, 34: 1377, 35: 81, 36: 1}

# colin = dice(6, 6)
# print(colin)
# colin = {21: 195528, 16: 90477, 17: 120096, 18: 148716, 19: 173196,
#          20: 189396, 22: 189396, 13: 24876, 14: 41526, 15: 63656,
#          12: 13541, 23: 173196, 24: 148716, 10: 2826, 11: 6552, 9: 976,
#          25: 120096, 26: 90477, 27: 63656, 8: 261, 7: 36,
#          28: 41526, 29: 24876, 30: 13541, 31: 6552, 6: 1,
#          32: 2826, 33: 976, 34: 261, 35: 36, 36: 1}

# n_peter_rolls = (sum(v for k, v in peter.items()))
# n_colin_rolls = (sum(v for k, v in colin.items()))
# # get the proability
#
# print("\nCOLIN", colin, n_colin_rolls)
# print("\nPETER", peter, n_peter_rolls)
#
# all_stuff = (n_colin_rolls*n_peter_rolls)
#
# def pete_wins_with(n):
#     # for key, val in colin.items():
#     #     if n > key:
#     #         something += val
#     return sum(val for key, val in colin.items() if n > key)
#
# def p205():
#     shit = sum(pete_wins_with(key) for key in peter.keys())
#
#     probs = []
#     print(shit)
#     print(all_stuff)
#     print((shit / n_peter_rolls))
#     print((shit / n_colin_rolls))
#
# print(p205())
#
# # peter_prob = {k:(v/n_peter_rolls) for k, v in peter.items()}
# # print(peter_prob)
# # colin_prob = {k:(v/n_colin_rolls) for k, v in colin.items()}
# # print(colin_prob)
#
#
#
#
#
#
#
#
#
#
#
#


