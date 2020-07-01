from poker import Rank
from poker import Suit
from collections import Counter

import numpy as np

def _3cardsSuited(hand ,flop, board, features):
    suitBoard = [x.suit for x in board]
    c = Counter(suitBoard)
    if c.most_common(1)[0][1] == 3 and\
        (c.most_common(1)[0][0] == hand.first.suit or c.most_common(1)[0][0] == hand.second.suit):
        features[38] = 1

def _4cardsSuited(hand ,flop, features):
    if hand.is_suited:
        if (hand.first.suit == flop[0].suit) \
            + (hand.first.suit == flop[1].suit) \
            + (hand.first.suit == flop[2].suit) == 2:
            features[39] = 1
    else:
        if ((hand.first.suit == flop[0].suit) 
        + (hand.first.suit == flop[1].suit) \
        + (hand.first.suit == flop[2].suit)) == 3 \
        or ((hand.second.suit == flop[0].suit) 
            + (hand.second.suit == flop[1].suit) \
            + (hand.second.suit == flop[2].suit)) == 3:
            features[39] = 1

def monoColorFlushNoDraw(hand ,flop, board, features):
    # Monochromatic flush
    if flop[0].suit == flop[1].suit and flop[0].suit == flop[2].suit:
        suitBoard = [x.suit for x in board]
        c = Counter(suitBoard)
        if c.most_common(1)[0][1] == 3:
            features[40] = 1
        

def biColorFlushNoDraw(hand ,flop, features):
    # Bichromatic flush with first card
    if (flop[0].suit == flop[1].suit and flop[0].suit != flop[2].suit) \
        or (flop[0].suit == flop[2].suit and flop[0].suit != flop[1].suit):
        if hand.is_suited and hand.first.suit == flop[0].suit: 
            features[41] = 1
    # Bichromatic flush without first card
    elif (flop[1].suit == flop[2].suit and flop[0].suit != flop[1].suit):
        if hand.is_suited and hand.first.suit == flop[1].suit: 
            features[41] = 1
    
def hasFlush(hand ,flop, features):
    if hand.is_suited and  hand.first.suit == flop[0].suit \
       and flop[0].suit == flop[1].suit and flop[0].suit == flop[2].suit:
        features[42] = 1
        features[45] = 1 # At least three of kind
        features[47] = 1 #At least two pairs

def FlushDraws(hand ,flop, board,features):
    _3cardsSuited(hand ,flop, board, features)
    _4cardsSuited(hand ,flop, features)
    monoColorFlushNoDraw(hand ,flop, board, features)
    biColorFlushNoDraw(hand ,flop, features)
    hasFlush(hand ,flop, features)