from poker import Rank
from poker import Suit
from collections import Counter

import numpy as np


def CheckStraightOnTheFlop(board, features):
    rankBoard = [x.rank for x in board]
    if len(set(rankBoard)) == 5 and\
        Rank.difference(rankBoard[0], rankBoard[1]) == 1 and Rank.difference(rankBoard[0], rankBoard[2]) == 2 and\
        Rank.difference(rankBoard[0], rankBoard[3]) == 3 and Rank.difference(rankBoard[0], rankBoard[4]) == 4:
        features[58] = 1
        features[45] = 1 #At least 3 of kind
    elif set([x.rank for x in board]) == {Rank('A'), Rank('2'), Rank('3'), Rank('4'), Rank('5')}:
        features[58] = 1
        features[45] = 1 #At least 3 of kind
        features[47] = 1 #At least two pairs

def OpenEndedStraightDraw(hand, board, features):
    rankBoard = [x.rank for x in board]
    if Rank.difference(rankBoard[0], rankBoard[1]) == 1 and Rank.difference(rankBoard[0], rankBoard[2]) == 2 and Rank.difference(rankBoard[0], rankBoard[3]) == 3 :
        if hand.second.rank == rankBoard[3]:
            features[59] = 1
        else:
            features[60] = 1
    elif Rank.difference(rankBoard[1], rankBoard[2]) == 1 and Rank.difference(rankBoard[1], rankBoard[3]) == 2 and Rank.difference(rankBoard[1], rankBoard[4]) == 3 :
        if hand.second.rank == rankBoard[4]:
            features[59] = 1
        else:
            features[60] = 1

def InsideStraighDraw(board, features):
    rankBoard = [x.rank for x in board]
    if Rank.difference(rankBoard[0], rankBoard[1]) == 2 and Rank.difference(rankBoard[0], rankBoard[2]) == 3 and Rank.difference(rankBoard[0], rankBoard[3]) == 4:
        features[61] = 1
    elif Rank.difference(rankBoard[0], rankBoard[1]) == 1 and  Rank.difference(rankBoard[0], rankBoard[2]) == 3 and Rank.difference(rankBoard[0], rankBoard[3]) == 4:
        features[61] = 1
    elif Rank.difference(rankBoard[0], rankBoard[1]) == 1 and Rank.difference(rankBoard[0], rankBoard[2]) == 2 and Rank.difference(rankBoard[0], rankBoard[3]) == 4:
        features[61] = 1

def DoubleInsideStraightDraw(board, features):
    rankBoard = [x.rank for x in board]
    if Rank.difference(rankBoard[0], rankBoard[1]) == 2 and Rank.difference(rankBoard[1], rankBoard[2]) == 1 \
        and Rank.difference(rankBoard[2], rankBoard[3]) == 1 and Rank.difference(rankBoard[3], rankBoard[4]) == 2:
        features[62] = 1; features[61] = 0

def OneWayBackdoorStraightDraw(board, features):
    rankBoard = [x.rank for x in board]
    # 2 cards in sequence + gap + 1 card
    if (Rank.difference(rankBoard[0], rankBoard[1]) == 1 and Rank.difference(rankBoard[0], rankBoard[2]) == 4)\
        or (Rank.difference(rankBoard[1], rankBoard[2]) == 1 and Rank.difference(rankBoard[1], rankBoard[3]) == 4)\
        or (Rank.difference(rankBoard[2], rankBoard[3]) == 1 and Rank.difference(rankBoard[2], rankBoard[4]) == 4):
        features[63] = 1
    # 1 card + gap + 2 cards in row
    elif (Rank.difference(rankBoard[0], rankBoard[1]) == 3 and Rank.difference(rankBoard[0], rankBoard[2]) == 4)\
        or (Rank.difference(rankBoard[1], rankBoard[2]) == 3 and Rank.difference(rankBoard[1], rankBoard[3]) == 4)\
        or (Rank.difference(rankBoard[2], rankBoard[3]) == 3 and Rank.difference(rankBoard[2], rankBoard[4]) == 4):
        features[63] = 1
    # 1 card + gap + 1 card + gap + 1 card
    elif (Rank.difference(rankBoard[0], rankBoard[1]) == 2 and Rank.difference(rankBoard[0], rankBoard[2]) == 4)\
        or (Rank.difference(rankBoard[1], rankBoard[2]) == 2 and Rank.difference(rankBoard[1], rankBoard[3]) == 4)\
        or (Rank.difference(rankBoard[2], rankBoard[3]) == 2 and Rank.difference(rankBoard[2], rankBoard[4]) == 4):
        features[63] = 1

def TwoMoreWaysBackdoorStraightDraw(board, features):
    rankBoard = [x.rank for x in board]
    # 2 cards in row + gap + 1 card + gap + 1 card
    if (Rank.difference(rankBoard[0], rankBoard[1]) == 1 and Rank.difference(rankBoard[0], rankBoard[2]) == 3 and Rank.difference(rankBoard[0], rankBoard[3]) == 5)\
        or (Rank.difference(rankBoard[1], rankBoard[2]) == 1 and Rank.difference(rankBoard[1], rankBoard[3]) == 3 and Rank.difference(rankBoard[1], rankBoard[4]) == 5):
        features[64] = 1; features[63] = 0
    elif (Rank.difference(rankBoard[0], rankBoard[1]) == 2 and Rank.difference(rankBoard[0], rankBoard[2]) == 3 and Rank.difference(rankBoard[0], rankBoard[3]) == 5)\
        or (Rank.difference(rankBoard[1], rankBoard[2]) == 2 and Rank.difference(rankBoard[1], rankBoard[3]) == 3 and Rank.difference(rankBoard[1], rankBoard[4])) == 5:
        features[64] = 1; features[63] = 0
    elif (Rank.difference(rankBoard[0], rankBoard[1]) == 2 and Rank.difference(rankBoard[0], rankBoard[2]) == 4 and Rank.difference(rankBoard[0], rankBoard[3]) == 5)\
        or (Rank.difference(rankBoard[1], rankBoard[2]) == 2 and Rank.difference(rankBoard[1], rankBoard[3]) == 4 and Rank.difference(rankBoard[1], rankBoard[4]) == 5):
        features[64] = 1; features[63] = 0

def NoStraightOfFlushDraw(hand, board, features):
    rankBoard = [x.rank for x in board]
    suitBoard = [x.suit for x in board]
    c = Counter(suitBoard)

    if c[hand.first.suit] < 3 and c[hand.second.suit] < 3:
        features[65] = 1
    elif not ((Rank.difference(rankBoard[0], rankBoard[1]) > 0 and Rank.difference(rankBoard[0], rankBoard[1]) <= 4) and \
        (Rank.difference(rankBoard[0], rankBoard[2]) > 0 and Rank.difference(rankBoard[0], rankBoard[2]) <= 4))\
        and \
        not ((Rank.difference(rankBoard[1], rankBoard[2]) > 0 and Rank.difference(rankBoard[1], rankBoard[2]) <= 4) and \
        (Rank.difference(rankBoard[1], rankBoard[3]) > 0 and Rank.difference(rankBoard[1], rankBoard[3]) <= 4))\
        and \
        not ((Rank.difference(rankBoard[2], rankBoard[3]) > 0 and Rank.difference(rankBoard[2], rankBoard[3]) <= 4) and \
        (Rank.difference(rankBoard[2], rankBoard[4]) > 0 and Rank.difference(rankBoard[2], rankBoard[4]) <= 4)):
        features[65] = 1


def StraightDraws(hand, flop, board, features):
    CheckStraightOnTheFlop(board, features)
    OpenEndedStraightDraw(hand, board, features)
    InsideStraighDraw(board, features)
    DoubleInsideStraightDraw(board, features)
    OneWayBackdoorStraightDraw(board, features)
    TwoMoreWaysBackdoorStraightDraw(board, features)
    NoStraightOfFlushDraw(hand, board, features)