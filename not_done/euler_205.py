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
import random
from itertools import combinations
from tqdm import tqdm


n_four_dice = 9
four_side = [1, 2, 3, 4] * n_four_dice
print(four_side)

n_six_dice = 6
six_side = [1, 2, 3, 4, 5, 6] * n_six_dice

# sum = sum([1 for i in combinations(four_side, 9)])
# print(sum)

colin = 0
peter = 0
ties = 0
for combo in tqdm(combinations(four_side, 9)):
    curcolin = sum(combo)
    for c2 in combinations(six_side, 6):
        c2sum = sum(c2)
        if curcolin > c2sum: colin += 1
        elif c2sum > curcolin: peter  += 1
        else: ties += 1

print(colin)
print(peter)
print(ties)





# for i in range(10):
#     print(random.randint(1, 10))


# class DiceGame(object):
#     def __init__(self):
#         self.a = 0
#         self.b = 0
#         self.c = 0
#
#     # @staticmethod
#     @staticmethod
#     def roll1():
#         return (random.randint(1, 4), random.randint(1, 4), random.randint(
#             1, 4), random.randint(1, 4), random.randint(1, 4),
#                 random.randint(1, 4), random.randint(1, 4), random.randint(
#             1, 4), random.randint(1, 4))
#
#     # @staticmethod
#     @staticmethod
#     def roll2():
#         return (random.randint(1, 6), random.randint(1, 6), random.randint(1, 6),
#                 random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
#
#     def total_num_games(self):
#         return self.a + self.b + self.c
#
#     def get_stats(self):
#         print("____")
#         print("ties: {}".format(self.a))
#         print("pyr: {}".format(self.b))
#         print("cube: {}".format(self.c))
#         print("total games: {}".format(self.total_num_games()))
#         print("ties frac: {}".format(self.a / self.total_num_games()))
#         print("pyr frac: {}".format(self.b / self.total_num_games()))
#         print("cube frac: {}".format(self.c / self.total_num_games()))
#
#     def play_game(self):
#         pyr = sum(self.roll1())
#         cubes = sum(self.roll2())
#
#         if pyr == cubes:
#             self.a += 1
#         elif pyr > cubes:
#             self.b += 1
#         else:
#             self.c += 1
#
#
# g = DiceGame()
# g.play_game()
#
# for i in range(999999):
#     g.play_game()
#     if i % 10 == 0:
#         g.get_stats()
