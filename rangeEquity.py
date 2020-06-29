from poker import Card
from poker.hand import Hand, Combo, Range

import holdem_calc
import numpy as np

suit_dict = {'♠': 's', '♣': 'c', '♥': 'h', '♦': 'd'}
groups = ['',
        'AA, KK, QQ, JJ, AKs ',
        'TT, AQs, AJs, KQs, AKo ',
        '99, AQo, ATs, KJs, QJs, JTs ',
        'T9s, KQo, 88, QTs, 98s, J9s, AJo, KTs ',
        '77, 87s, Q9s, T8s, KJo, QJo, JTo, 76s, 97s, A9s-, 65s ',
        '66, ATo, 55, 86s, KTo, QTo, 54s, K9s , J8s, 75s ',
        '44, J9o, 64s, T9o, 53s, 33, 98o, 43s , 22, K9s-, K2s ',
        '87, A9o, Q9o, 76o, 42s, 32s, 96s, 85s , J8o, J7s, 65o, 54o, 74s, K9o, T8o '
        ]

RUS = Range(groups[1])
RS = Range(groups[1]+groups[2])
RML = Range(groups[1]+groups[2]+groups[3]+groups[4]+groups[5])
ATC = Range('XX')

def card2str(card: Card)-> str:
    return(str(card.rank) + suit_dict[str(card.suit)])

def combo2str(combo: Combo)-> str:
    return ([str(combo.first.rank) + suit_dict[str(combo.first.suit)],
             str(combo.second.rank) + suit_dict[str(combo.second.suit)]])

def is_hand_consistent(hand, hand_reference):
    return not (hand[0] in hand_reference or hand[1] in hand_reference)

def are_cards_consistent(board, hero_cards, villan_cards):
    return (is_hand_consistent(hero_cards, board) and 
            is_hand_consistent(villan_cards, board) and 
            is_hand_consistent(hero_cards, villan_cards) )


# calculate odds hero against villan 
def calculate_odds_villan(hero_cards, board, villan_cards):
    hero_cards = combo2str(hero_cards)
   
    if villan_cards is None:
        villan_cards = ["?", "?"]
    else:
        villan_cards = combo2str(villan_cards)
    players_cards = hero_cards + villan_cards
    if(not are_cards_consistent(board, hero_cards, villan_cards)):
        return None    
    return holdem_calc.calculate(board, True, 1, None, players_cards, False)

def E(hand, board, villan_range):
    odds = [calculate_odds_villan(hand, board, villan_hand) for villan_hand in villan_range.combos]
    return np.mean([case[0] for case in odds if case]) + np.mean([case[1] for case in odds if case])


