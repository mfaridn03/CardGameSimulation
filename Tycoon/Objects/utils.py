# Tycoon hand utilities
import typing

from Objects.consts import *


def sort_hand(cards: typing.Sequence[str], is_rev=False) -> None:
    """
    Sort the cards in the hand
    Suit order: D C H S
    Rank order: 3 4 5 6 7 8 9 10 J Q K A 2
    
    If reversed, the order is
    Suit order: D C H S
    Rank order: 2 A K Q J 10 9 8 7 6 5 4 3
    
    Jokers are placed in the rightmost positions
    """
    temp_cards = []
    if JOKER_RED in cards:
        temp_cards.append(JOKER_RED)
        cards.remove(JOKER_RED)
    if JOKER_BLACK in cards:
        temp_cards.append(JOKER_BLACK)
        cards.remove(JOKER_BLACK)
    
    if (is_rev):
        cards.sort(key=lambda card: (RANK_ORDER_REV.index(card[0]), SUIT_ORDER.index(card[1])))
    else:
        cards.sort(key=lambda card: (RANK_ORDER.index(card[0]), SUIT_ORDER.index(card[1])))
        
    for card in temp_cards:
        cards.append(card)
    
def is_joker(card: str) -> bool:
    """
    Check if a card is a Joker
    """
    return card == JOKER_RED or card == JOKER_BLACK

def has_joker(cards: typing.Sequence[str]) -> bool:
    """
    Check if a list of cards contains a Joker
    """
    return JOKER_RED in cards or JOKER_BLACK in cards

def is_pair(cards: typing.Sequence[str]) -> bool:
    """
    Check if the cards are a pair
    """
    cards = sort_hand(cards)
    found_joker = is_joker(cards[0]) or is_joker(cards[1])
    ranks_match = cards[0][0] == cards[1][0]
    return len(cards) == 2 and (ranks_match or found_joker)


def is_triple(cards: list):
    """
    Check if the cards are a triple
    """
    if len(cards) != 3:
        return False
    
    temp_cards = [card for card in cards]
    if JOKER_RED in temp_cards:
        temp_cards.remove(JOKER_RED)
    if JOKER_BLACK in temp_cards:
        temp_cards.remove(JOKER_BLACK)
    
    # Isolate ranks of each remaining card, and form a set of these ranks
    # Sets contain only unique values, so common ranks will be combined into one item
    # Set size of 1 means that all ranks are common so we have a triple
    rank_set = set([card[0] for card in temp_cards])
    return len(rank_set) == 1

def is_revolution(cards: list) -> bool:
    """
    Check if the cards are a revolution
    """
    if len(cards) != 4:
        return False
    
    temp_cards = [card for card in cards]
    if JOKER_RED in temp_cards:
        temp_cards.remove(JOKER_RED)
    if JOKER_BLACK in temp_cards:
        temp_cards.remove(JOKER_BLACK)
    
    # Isolate ranks of each remaining card, and form a set of these ranks
    # Sets contain only unique values, so common ranks will be combined into one item
    # Set size of 1 means that all ranks are common so we have a revolution
    rank_set = set([card[0] for card in temp_cards])
    return len(rank_set) == 1


def is_higher_play(is_this_higher: list, than_this: list):
    if len(is_this_higher) == 1:
        return get_card_score(is_this_higher) > get_card_score(than_this)

    elif len(is_this_higher) == 2:
        return get_pair_score(is_this_higher) > get_pair_score(than_this)

    elif len(is_this_higher) == 3:
        return get_triple_score(is_this_higher) > get_triple_score(than_this)


def get_card_score(card: list) -> int:
    """
    Get the score of a card
    """
    card_string = card[0]
    return RANK_ORDER.index(card_string[0]), SUIT_ORDER.index(card_string[1])


def get_pair_score(pair: list) -> int:
    """
    Get the score of a pair
    """
    rank = RANK_ORDER.index(pair[0][0])
    suit_scores = [SUIT_ORDER.index(pair[x][1]) for x in range(2)]
    return rank, max(suit_scores)


def get_triple_score(triple: list) -> int:
    """
    Get the score of a triple
    """
    rank = RANK_ORDER.index(triple[0][0])
    suit_scores = [SUIT_ORDER.index(triple[x][1]) for x in range(3)]
    return rank, max(suit_scores)


def is_higher_revolution(is_this_higher: list, than_this: list) -> bool:
    """
    Check if this is a higher five
    """
    pass

