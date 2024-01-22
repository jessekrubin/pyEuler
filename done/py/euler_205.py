#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Dice Game
Problem 205
Peter has nine four-sided (pyramidal) dice, each w/ faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each w/ faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins.
The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin?
(Give your answer rounded to seven decimal places in the form 0.abcdefg)
"""
from __future__ import division
from itertools import product


def dice_combos(n_dice, faces):
    rolls = {val: set() for val in range(n_dice, n_dice * faces + 1)}
    for roll in product(list((range(1, faces + 1))), repeat=n_dice):
        rolls[sum(roll)].add(roll)
    roll_vals = {roll_sum: len(combos) for roll_sum, combos in rolls.items()}
    return roll_vals


def p205():
    pete = dice_combos(9, 4)
    colin = dice_combos(6, 6)
    p_wins = 0
    ties = 0
    c_wins = 0
    for pete_roll_sum, pete_rolls in pete.items():
        for colin_roll_sum, colin_rolls in colin.items():
            if pete_roll_sum == colin_roll_sum:
                ties += pete_rolls * colin_rolls
            elif pete_roll_sum > colin_roll_sum:
                p_wins += pete_rolls * colin_rolls
            elif pete_roll_sum < colin_roll_sum:
                c_wins += pete_rolls * colin_rolls

    return round(p_wins / (p_wins + c_wins + ties), ndigits=7)


if __name__ == "__main__":
    ANSWER = p205()
    print("Probability that Pyramidal Pete Wins: {}".format(ANSWER))
