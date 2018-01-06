# coding=utf-8
# Dice Game
# Problem 205
# Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
# Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

# Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

# What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg

import random

# for i in range(10):
#     print(random.randint(1, 10))


class DiceGame(object):
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    # @staticmethod
    def roll1(self):
        return (random.randint(1, 4), random.randint(1, 4), random.randint(
            1, 4), random.randint(1, 4), random.randint(1, 4),
                random.randint(1, 4), random.randint(1, 4), random.randint(
                    1, 4), random.randint(1, 4))

    # @staticmethod
    def roll2(self):
        return (random.randint(1, 6), random.randint(1, 6), random.randint(1, 6),
                random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))

    def totaNumGames(self):
        return (self.a + self.b +self.c)

    def get_stats(self):
        print("____")
        print("ties: {}".format(self.a))
        print("pyr: {}".format(self.b))
        print("cube: {}".format(self.c))
        print("total games: {}".format(self.totaNumGames()))
        print("ties frac: {}".format(self.a /self.totaNumGames()))
        print("pyr frac: {}".format(self.b / self.totaNumGames()))
        print("cube frac: {}".format(self.c / self.totaNumGames()))

    def playGame(self):
        pyr = sum(self.roll1())
        cubes = sum(self.roll2())

        if pyr==cubes:
            self.a += 1
        elif pyr > cubes:
            self.b += 1
        else:
            self.c += 1




g = DiceGame()
g.playGame()

for i in range(999999):
    g.playGame()
    if i % 10 == 0:
        g.get_stats()