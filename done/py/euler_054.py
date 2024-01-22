#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Poker hands
Problem 54
In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD   2C 3S 8S 8D TD     Player 2
        Pair of Fives    Pair of Eights

2	 	5D 8C 9S JS AC   2C 5C 7D 8S QH     Player 1
        High card Ace    High card Queen

3	 	2D 9C AS AH AC   3D 6D 7D TD QD     Player 2
        Three Aces       Flush w/ Diamonds

4	 	4D 6S 9H QH QC   3D 6D 7H QD QS     Player 1
        Pair of Queens   Pair of Queens
        High card Nine   High card Seven

5	 	2H 2D 4C 4D 4S   3C 3D 3S 9S 9D     Player 1
        Full House       Full House
        w/ Three Fours    w/ Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?
"""
from collections import Counter


class Card(object):
    def __init__(self, val, suit, strang):
        self.val = val
        self.suit = suit
        self.strang = strang

    @classmethod
    def string_to_card(self, strang):
        chars = [c for c in strang]
        val = 0
        suit = chars[1]
        try:
            val = int(chars[0])
        except ValueError:
            if chars[0] == "T":
                val = 10
            elif chars[0] == "J":
                val = 11
            elif chars[0] == "Q":
                val = 12
            elif chars[0] == "K":
                val = 13
            elif chars[0] == "A":
                val = 14
        return Card(val, suit, strang)

    def __str__(self):
        return self.strang

    def __repr__(self):
        return self.strang


class PokerHand(object):
    def __init__(self, cards):
        self.cards = cards
        self.suits_counter = Counter(card.suit for card in cards)
        self.vals_counter = Counter(card.val for card in cards)
        self.rank_counter = self.evaluate_rank()

    def evaluate_rank(self):
        """
        0 --- High Card: Highest value card.
        1 --- One Pair: Two cards of the same value.
        2 --- Two Pairs: Two different pairs.
        3 --- Three of a Kind: Three cards of the same value.
        4 --- Straight: All cards are consecutive values.
        5 --- Flush: All cards of the same suit.
        6 --- Full House: Three of a kind and a pair.
        7 --- Four of a Kind: Four cards of the same value.
        8 --- Straight Flush: All cards are consecutive values of same suit.
        8.5 --- Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
        """
        rank_counter = Counter()
        rank_counter[0] = max(v for v in self.vals_counter.keys())
        low_card = min(v for v in self.vals_counter.keys())

        for val, count in self.vals_counter.items():
            if count == 4:
                rank_counter[7] = val
            if count == 3:
                rank_counter[3] = val
            if count == 2 and 1 not in rank_counter:
                rank_counter[1] = val
            if count == 2 and 1 in rank_counter:
                if val > rank_counter[1]:
                    rank_counter[2] = val
                elif val < rank_counter[1]:
                    temp = rank_counter[1]
                    rank_counter[1] = val
                    rank_counter[2] = temp

        # check for full house
        if 3 in rank_counter and 1 in rank_counter:
            rank_counter[6] = rank_counter[3]

        # check for flushes and straights
        flush = True if len(self.suits_counter) == 1 else False

        if 14 in self.vals_counter.keys() and 2 in self.vals_counter.keys():
            straight = (
                True if set(self.vals_counter.keys()) == {2, 3, 4, 5, 14} else False
            )
        else:
            straight = (
                True
                if len(self.vals_counter) == 5 and rank_counter[0] - (low_card - 1) == 5
                else False
            )

        if flush and straight:  # don't really need to deal with rank 9
            if rank_counter[0] == 14 and low_card == 10:
                rank_counter[9] = rank_counter[0]
            else:
                rank_counter[8] = rank_counter[0]
        elif flush and not straight:
            rank_counter[5] = rank_counter[0]
        elif not flush and straight:
            if 14 in self.vals_counter.keys() and 2 in self.vals_counter.keys():
                rank_counter[4] = 5
            else:
                rank_counter[4] = rank_counter[0]
        return rank_counter

    def __str__(self):
        return " ".join(c.__str__() for c in self.cards)

    def __repr__(self):
        return " ".join(c.__str__() for c in self.cards)

    def __gt__(self, p2_hand):
        for rank in range(9, -1, -1):
            if rank in self.rank_counter and rank not in p2_hand.rank_counter:
                return True
            if rank not in self.rank_counter and rank in p2_hand.rank_counter:
                return False
            if rank in self.rank_counter and rank in p2_hand.rank_counter:
                if self.rank_counter[rank] > p2_hand.rank_counter[rank]:
                    return True
                elif self.rank_counter[rank] < p2_hand.rank_counter[rank]:
                    return False
        return None


with open("../../txt_files/p054_poker.txt") as f:
    games = [game.strip("\n").split(" ") for game in f.readlines()]


def p054():
    p1_wins = 0
    for g in games:
        for c in g:
            Card.string_to_card(c)
        player_1 = PokerHand(
            [Card.string_to_card(card_string) for card_string in g[:5]]
        )
        player_2 = PokerHand(
            [Card.string_to_card(card_string) for card_string in g[5:]]
        )
        if player_1 > player_2:
            p1_wins += 1
    return p1_wins


if __name__ == "__main__":
    answer = p054()
    print("Player 1 wins {} times".format(answer))
