from poker import Rank

import numpy as np

def straightFlop(flop, features):
    # Three consectuive cards
    if Rank.difference(flop[0].rank, flop[1].rank) == 1 and Rank.difference(flop[1].rank, flop[2].rank) == 1:
        features[33] = 1
    # 1-gap flop
    elif (Rank.difference(flop[0].rank, flop[1].rank) == 1 and Rank.difference(flop[0].rank, flop[2].rank) == 3) or (Rank.difference(flop[0].rank, flop[1].rank) == 2 and Rank.difference(flop[0].rank, flop[2].rank) == 3):
        features[34] = 1
    # 2-gap flop
    elif (Rank.difference(flop[0].rank, flop[1].rank) == 1 and Rank.difference(flop[0].rank, flop[2].rank) == 4) or (Rank.difference(flop[0].rank, flop[1].rank) == 3 and Rank.difference(flop[0].rank, flop[2].rank) == 4) or (Rank.difference(flop[0].rank, flop[1].rank) == 2 and Rank.difference(flop[0].rank, flop[2].rank) == 4) or (Rank.difference(flop[0].rank, flop[1].rank) == 0 and Rank.difference(flop[0].rank, flop[2].rank) == 3) or (Rank.difference(flop[1].rank, flop[2].rank) == 0 and Rank.difference(flop[0].rank, flop[1].rank) == 3):
        features[35] = 1
    # 3-gap flop
    elif (Rank.difference(flop[0].rank, flop[1].rank) == 4 and Rank.difference(flop[0].rank, flop[2].rank) == 5) or (Rank.difference(flop[0].rank, flop[1].rank) == 1 and Rank.difference(flop[0].rank, flop[2].rank) == 5) or (Rank.difference(flop[0].rank, flop[1].rank) == 0 and Rank.difference(flop[0].rank, flop[2].rank) == 4) or (Rank.difference(flop[0].rank, flop[1].rank) == 0 and Rank.difference(flop[0].rank, flop[2].rank) == 4) or (Rank.difference(flop[1].rank, flop[2].rank) == 0 and Rank.difference(flop[0].rank, flop[1].rank) == 4):
        features[36] = 1
    # no straight or straight draw in the flop
    else:
        features[37] = 1

