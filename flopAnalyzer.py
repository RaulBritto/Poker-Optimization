from poker import Card

import numpy as np
import Broadway
import Suits
import Ranks
import Straight

features = np.zeros(73, dtype=bool)


def sortFlop(flop):
    sortedFlop = []
    if flop[0].rank > flop[1].rank and flop[0].rank > flop[2].rank:
        sortedFlop.append(flop[0])
        if flop[1].rank > flop[2].rank:
            sortedFlop.append(flop[1])
            sortedFlop.append(flop[2])
        else:
            sortedFlop.append(flop[2])
            sortedFlop.append(flop[1])

    elif flop[1].rank > flop[0].rank and flop[1].rank > flop[2].rank:
        sortedFlop.append(flop[1])
        if flop[0].rank > flop[2].rank:
            sortedFlop.append(flop[0])
            sortedFlop.append(flop[2])
        else:
            sortedFlop.append(flop[2])
            sortedFlop.append(flop[0])
    else:
        sortedFlop.append(flop[2])
        if flop[0].rank > flop[1].rank:
            sortedFlop.append(flop[0])
            sortedFlop.append(flop[1])
        else:
            sortedFlop.append(flop[1])
            sortedFlop.append(flop[0])
    
    return sortedFlop
    



def FlopFeatures(flop):
    sortedFlop = sortFlop(flop)
    Broadway.BroadwayCards(sortedFlop, features)
    Suits.SuitsCards(sortedFlop, features)
    Ranks.RankCards(sortedFlop, features)
    Straight.straightFlop(sortedFlop, features)

    return features