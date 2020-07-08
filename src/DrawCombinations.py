from poker import Rank
from collections import Counter

import numpy as np

def InsideStraightDrawAndOvercards(features):
    if features[61]:
        if not features[56] and not features[57]:
            features[66] = 1
        elif features[56] and not features[57]:
            features[67] = 1
        elif not features[56] and features[57]:
            features[68] = 1

def InsideStraightDrawAndFlushBackdoor(hand, flop, board, features):
    # Inside Straight Draw
    if features[61]:
        suitBoard = [x.suit for x in board]
        c = Counter(suitBoard)
        # Backdoor Flush
        if c[hand.first.suit] == 3 or c[hand.second.suit] == 3\
            and Counter([x.suit for x in flop]).most_common(1)[0][1] >= 2:
            features[69] = 1

def InsideStraightDrawAndFlushDraw(features):
    # Inside Straight Draw and flush draw
    if features[61] and features[39]:
        features[70] = 1

def FlushDrawAndOverCards(features):
    # Flush draw and 
    if features[39] and features[56]:
        features[71] = 1
    elif features[39] and features[57]:
        features[72] = 1


def CheckDrawCombinations(hand, flop, board, features):
    InsideStraightDrawAndOvercards(features)
    InsideStraightDrawAndFlushBackdoor(hand, flop, board, features)
    InsideStraightDrawAndFlushDraw(features)
    FlushDrawAndOverCards(features)
   
