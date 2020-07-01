from poker import Rank

import numpy as np

def flopOvercards(hand, flop, features):
    numOvercards = (hand.first.rank < flop[0].rank) + (hand.first.rank < flop[1].rank) + (hand.first.rank < flop[2].rank)
    if numOvercards == 0:
        features[53] = 1
    elif numOvercards == 1:
        features[54] = 1
    elif numOvercards >= 2:
        features[55] = 1

def handOvercards(hand, flop, features):
    numOvercards = (hand.first.rank > flop[0].rank) + (hand.second.rank > flop[0].rank)
    if numOvercards == 1:
        features[56] = 1
    elif numOvercards == 2:
        features[57] = 1

def CheckOvercards(hand, flop, features):
    flopOvercards(hand, flop, features)
    handOvercards(hand, flop, features)

