from poker import Rank

import numpy as np

def checkSameRank(flop, features):
    if (flop[0].rank == flop[1].rank) + (flop[1].rank == flop[2].rank) == 2:
        features[19] = 1
    elif (flop[0].rank == flop[1].rank) + (flop[0].rank == flop[2].rank) + (flop[1].rank == flop[2].rank) == 1:
        features[20] = 1
    else:
        features[21] = 1

def paintCards(flop, features):
    numPaints = (flop[0].rank >= Rank('J')) + (flop[1].rank >= Rank('J')) + (flop[2].rank >= Rank('J'))
    if numPaints == 1:
        features[22] = 1
    elif numPaints == 2:
        features[23] = 1
    elif numPaints == 3:
        features[25]

def mediumSizeCards(flop, features):
    if ( (flop[0].rank <= Rank('T') and flop[0].rank >= Rank('7')) 
        + (flop[1].rank <= Rank('T') and flop[1].rank >= Rank('7')) 
        + (flop[2].rank <= Rank('T') and flop[2].rank >= Rank('7')) ) == 3:
        features[29] = 1

def smallSizeCards(flop, features):
    if ( (flop[0].rank <= Rank('6') and flop[0].rank >= Rank('2')) 
        + (flop[1].rank <= Rank('6') and flop[1].rank >= Rank('2')) 
        + (flop[2].rank <= Rank('6') and flop[2].rank >= Rank('2')) ) == 3:
        features[30] = 1
    
def medium_smallSizeCards(flop, features):
    if ( (flop[0].rank <= Rank('T') and flop[0].rank >= Rank('2')) 
        + (flop[1].rank <= Rank('T') and flop[1].rank >= Rank('2')) 
        + (flop[2].rank <= Rank('T') and flop[2].rank >= Rank('2')) ) == 3:
        features[31] = 1

def differentSmallCards(flop, features):
    if ((flop[0].rank <= Rank('5')) + (flop[1].rank <= Rank('5') ) + (flop[2].rank <= Rank('5'))) == 3 and features[21]:
        features[32] = 1


def RankCards(flop, features):
    checkSameRank(flop, features)
    paintCards(flop, features)
    mediumSizeCards(flop, features)
    smallSizeCards(flop, features)
    medium_smallSizeCards(flop, features)
    differentSmallCards(flop, features)