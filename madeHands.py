from poker import Rank
from collections import Counter
import numpy as np


def _4ofKind_Or_FullHouse(board, features):
    # 4-of-kind or full-house
    if len(set([x.rank for x in board])) == 2 :
        features[43] = 1
        features[45] = 1 #At least 3 of kind
        features[47] = 1 #At least two pairs
        
def _3ofKindOneStartingHand(board, hand, features):
    b = [str(x.rank) for x in board]
    # Check if there is a 3 of kind 
    if len(set(b)) == 3 and Counter(b).most_common(1)[0][1] == 3:
        # The 3-of-kind using a hand card
        if str(hand.first.rank) == Counter(b).most_common()[0][0] \
            or str(hand.second.rank) == Counter(b).most_common()[0][0]:
            features[44] = 1

def atLeast3ofKindOneStartingHand(board, hand, features):
    # Check if there is a 3 of kind
    if features[44]:
        features[45] = 1
        features[47] = 1 #At least two pairs
    
def PairedOneofCards(flop, hand, features):
    if len( [x for x in flop if x.rank == hand.first.rank] + [x for x in flop if x.rank == hand.second.rank] ) == 1:
        features[46] = 1

def _2Pairs(board, features):
    b = [str(x.rank) for x in board]
    if Counter(b).most_common(2)[0][1] == 2 and Counter(b).most_common(2)[1][1] == 2:
        features[47] = 1

def FlopHighPair(flop, hand, features):
    # All cards on flop are differents and not paired hand
    if features[21] and not hand.is_suited:
        if hand.first.rank == flop[0].rank or hand.second.rank == flop[0].rank:
            features[48] = 1

def FlopMediumPair(flop, hand, features):
    # All cards on flop are differents and not paired hand
    if features[21] and not hand.is_suited:
        if hand.first.rank == flop[1].rank or hand.second.rank == flop[1].rank:
            features[49] = 1

def FlopBottomPair(flop, hand, features):
    # All cards on flop are differents and not paired hand
    if features[21] and not hand.is_suited:
        if hand.first.rank == flop[2].rank or hand.second.rank == flop[2].rank:
            features[50] = 1

def _2Pairs_3ofKind_flop_3_ranks(flop, hand, features):
    if (features[47] or features[44]) and features[21]:
        features[51] = 1


def _2Pairs_3ofKind_flop_2_ranks(flop, hand, features):
    if (features[47] or features[44]) and features[20]:
        features[52] = 1
        

def checkMadeHands(hand, flop, board, features):
    _4ofKind_Or_FullHouse(board, features)
    _3ofKindOneStartingHand(board, hand, features)
    atLeast3ofKindOneStartingHand(board, hand, features)
    PairedOneofCards(flop, hand, features)
    _2Pairs(board, features)
    FlopHighPair(flop, hand, features)
    FlopMediumPair(flop, hand, features)
    FlopBottomPair(flop, hand, features)
    _2Pairs_3ofKind_flop_3_ranks(flop, hand, features)
    _2Pairs_3ofKind_flop_2_ranks(flop, hand, features)