from poker import Card

import numpy as np
import Broadway
import Suits
import Ranks
import Straight
import flushDraw
import madeHands
import Overcards
import StraightDraw
import DrawCombinations

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
    
def sortBoard(flop, hand):
    board = flop.copy()
    if hand.first > flop[0]:
        board.insert(0, hand.first)
    elif hand.first > flop[1]:
        board.insert(1, hand.first)
    elif hand.first > flop[2]:
        board.insert(2, hand.first)
    else:
        board.append(hand.first)
    
    if hand.second > flop[0]:
            board.insert(1, hand.second)
    elif hand.second > flop[1]:
        board.insert(2, hand.second)
    elif hand.second > flop[2]:
        board.insert(3, hand.second)
    else:
        board.append(hand.second)
    
    return board


def FlopFeatures(hand, flop):

    sortedFlop = sortFlop(flop)
    board = sortBoard(sortedFlop, hand)

    # Features entirely on the flop
    Broadway.BroadwayCards(sortedFlop, features)
    Suits.SuitsCards(sortedFlop, features)
    Ranks.RankCards(sortedFlop, features)
    Straight.straightFlop(sortedFlop, features)
    
    # Features combining flop and hand
    flushDraw.FlushDraws(hand , sortedFlop, board, features)
    madeHands.checkMadeHands(hand, sortedFlop, board, features)
    Overcards.CheckOvercards(hand, flop, features)
    StraightDraw.StraightDraws(hand, sortedFlop, board, features)
    DrawCombinations.CheckDrawCombinations(hand, sortedFlop, board, features)

    return features



