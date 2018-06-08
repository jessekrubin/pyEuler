#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse Rubin ~ project Euler ~
"""
The Roundtable Lottery
http://projecteuler.net/problem=444
A group of p people decide to sit down at a round table and play a lottery-ticket trading game. Each person starts off with a randomly-assigned, unscratched lottery ticket. Each ticket, when scratched, reveals a whole-pound prize ranging anywhere from £1 to £p, with no two tickets alike. The goal of the game is for each person to maximize his ticket winnings upon leaving the game.
An arbitrary person is chosen to be the first player. Going around the table, each player has only one of two options:
1. The player can scratch his ticket and reveal its worth to everyone at the table.
2. The player can trade his unscratched ticket for a previous player's scratched ticket, and then leave the game with that ticket. The previous player then scratches his newly-acquired ticket and reveals its worth to everyone at the table.
The game ends once all tickets have been scratched. All players still remaining at the table must leave with their currently-held tickets.
Assume that each player uses the optimal strategy for maximizing the expected value of his ticket winnings.
Let E(p) represent the expected number of players left at the table when the game ends in a game consisting of p players (e.g. E(111) = 5.2912 when rounded to 5 significant digits).
Let S1(N) =  E(p)
Let Sk(N) =  Sk-1(p) for k > 1
Find S20(1014) and write the answer in scientific notation rounded to 10 significant digits. Use a lowercase e to separate mantissa and exponent (e.g. S3(100) = 5.983679014e5).
"""

def p444():
    pass

if __name__ == '__main__':
    p444()