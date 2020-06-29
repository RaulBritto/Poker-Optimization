from poker import Card
from poker.hand import Hand, Combo, Range
from itertools import combinations

import rangeEquity
import numpy as np

heroHand = Combo('KcKs')
flop = ["Qc", "Th", "9s"] 
villan_range = Range('77+, AT+, KJ+')

pWin = np.zeros(19600)

#Create a deck
deck = list(Card)
#Remove the cards of the hero
deck = [ card for card in deck if card not in (heroHand.first, heroHand.second)]
#Create all possibles flops
comb = combinations(deck,3)
# For each combination calculates the real probability of win (tie + win)
for _combination ,flop in enumerate(list(comb)):

    if _combination == 10:
        break

    board = [rangeEquity.card2str(x) for x in flop]
    print(_combination ,rangeEquity.E(heroHand, board, villan_range))
    pWin [_combination]  = rangeEquity.E(heroHand, board, villan_range)

