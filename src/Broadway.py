from poker import Rank


import numpy as np

def checkAces(flop, features):
    numAces = (flop[0].rank == Rank('A')) + (flop[1].rank == Rank('A')) + (flop[2].rank == Rank('A'))
    if numAces == 1:
        features[0] = 1
    elif numAces >= 2: 
        features[1] = 1
    else:
        features[2] = 1 
    
def checkKings(flop, features):
    numKings = (flop[0].rank == Rank('K')) + (flop[1].rank == Rank('K')) + (flop[2].rank == Rank('K'))
    if numKings == 1:
        features[3] = 1
    elif numKings >= 2: 
        features[4] = 1
    else:
        features[5] = 1 

def checkQueens(flop, features):
    numQueens = (flop[0].rank == Rank('Q')) + (flop[1].rank == Rank('Q')) + (flop[2].rank == Rank('Q'))
    if numQueens == 1:
        features[6] = 1
    elif numQueens >= 2: 
        features[7] = 1
    else:
        features[8] = 1 

def checkJacks(flop, features):
    numJacks = (flop[0].rank == Rank('J')) + (flop[1].rank == Rank('J')) + (flop[2].rank == Rank('J'))
    if numJacks == 1:
        features[9] = 1
    elif numJacks >= 2: 
        features[10] = 1
    else:
        features[11] = 1 

def checkTens(flop, features):
    numTens = (flop[0].rank == Rank('T')) + (flop[1].rank == Rank('T')) + (flop[2].rank == Rank('T'))
    if numTens == 1:
        features[12] = 1
    elif numTens >= 2: 
        features[13] = 1
    else:
        features[14] = 1 

def checkNumberOfBroadway(flop, features):
    numBroadway = (flop[0].is_broadway) + (flop[1].is_broadway) + (flop[2].is_broadway)
    if numBroadway == 0:
        features[25] = 1
    elif numBroadway == 1:
        features[26] = 1
    elif numBroadway == 2:
        features[27] = 1
    else:
        features[28] = 1

def BroadwayCards(flop, features):
    checkAces(flop, features)
    checkKings(flop, features)
    checkQueens(flop, features)
    checkJacks(flop, features)
    checkTens(flop, features)
    checkNumberOfBroadway(flop, features)