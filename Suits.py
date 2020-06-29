from poker import Rank
from poker import Suit

import numpy as np

def checkSuitsFlop(flop, features):
    if (flop[0].suit == flop[1].suit) + (flop[1].suit == flop[2].suit) == 2:
        features[15] = 1
    elif (flop[0].suit == flop[1].suit) + (flop[0].suit == flop[2].suit) + (flop[1].suit == flop[2].suit) == 1:
        features[16] = 1
    else:
        features[17] = 1

def checkAceSuited(flop, features):
    if features[16] == 1:
        if flop[0].rank == Rank('A') and (flop[0].suit == flop[1].suit or flop[0].suit == flop[2].suit):
            features[18] = 1
            return None
        elif flop[1].rank == Rank('A') and (flop[1].suit == flop[0].suit or flop[1].suit == flop[2].suit):
            features[18] = 1
            return None
        elif flop[2].rank == Rank('A') and (flop[2].suit == flop[0].suit or flop[2].suit == flop[0].suit):
            features[18] = 1


def SuitsCards(flop, features):
    checkSuitsFlop(flop, features)
    checkAceSuited(flop, features)