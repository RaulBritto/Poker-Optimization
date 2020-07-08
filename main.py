from poker import Card
from poker.hand import Hand, Combo, Range
from itertools import combinations

import rangeEquity
import flopAnalyzer
import random
import argparse
import numpy as np

def analyze(heroHand, villan_range, iterations = 19600):

    vFeatures = np.ndarray((iterations,73),dtype = int)
    pWin = np.ndarray((iterations),dtype = float)

    #Create a deck
    deck = list(Card)
    #Remove the cards of the hero
    deck = [ card for card in deck if card not in (heroHand.first, heroHand.second)]
    random.shuffle(deck)
    #Create all possibles flops
    comb = combinations(deck,3)
    # For each combination calculates the real probability of win (tie + win)
    for _combination ,flop in enumerate(list(comb)):

        if _combination == iterations:
            break

        board = [rangeEquity.card2str(x) for x in flop]
        vFeatures[_combination] = flopAnalyzer.FlopFeatures(heroHand, flop)
        pWin[_combination] = rangeEquity.E(heroHand, board, villan_range)

    return vFeatures, pWin

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate the probability of a hero hand againts a defined villan\'s range.')
    parser.add_argument("--hand", required=True, help="set the hero hands cards. Example: \"JcJh\".")
    parser.add_argument("--range", help="set the villan's range. Example: [\"Qc\", \"Th\", \"9s\"].", required=True, type=str)
    parser.add_argument("-n", type=int, default = 19600, help="If you desire to define a fixed number of iterantions (Default value 19600)")
    
    args = parser.parse_args()
    heroHand = Combo(args.hand)
    range = str(args.range)
    villan_range = Range(range)
    n = args.n

    if args.n:
        n = args.n
        f, b = analyze(heroHand, villan_range, n)
    else:
        f, b = analyze(heroHand, villan_range)