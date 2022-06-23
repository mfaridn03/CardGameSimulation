# Poker hand utilities
import typing

from objectss.consts import *


def sort_hand(cards: typing.Sequence[str]) -> None:
    """
    Sort the cards in the hand
    Suit order: D C H S
    Rank order: 3 4 5 6 7 8 9 10 J Q K A 2
    """
    cards.sort(key=lambda card: (RANK_ORDER.index(card[0]), SUIT_ORDER.index(card[1])))


def is_pair(cards: list):
    """
    Check if the cards are a pair
    """
    cards = sort_hand(cards)
    return len(cards) == 2 and cards[0][0] == cards[1][0]


def is_triples(cards: list):
    """
    Check if the cards are a triple
    """
    cards = sort_hand(cards)
    return len(cards) == 3 and cards[0][0] == cards[1][0] == cards[2][0]


def is_straight(cards: list):
    hand = sort_hand(cards)

    # This is gonna be ugly
    def rank_score(card):
        return RANK_ORDER.index(card[0])

    if rank_score(hand[4]) - rank_score(hand[3]) == 1:
        if rank_score(hand[3]) - rank_score(hand[2]) == 1:
            if rank_score(hand[2]) - rank_score(hand[1]) == 1:
                if rank_score(hand[1]) - rank_score(hand[0]) == 1:
                    return True
    return False


def is_flush(cards: list):
    """
    Check if the cards are a flush
    """
    cards = sort_hand(cards)
    return (
        len(cards) == 5
        and cards[0][1] == cards[1][1] == cards[2][1] == cards[3][1] == cards[4][1]
    )


def is_full_house(cards: list) -> bool:
    """
    Check if the cards are a full house
    """
    cards = sort_hand(cards)
    ranks = {}
    for card in cards:
        if card[0] in ranks.keys():
            ranks[card[0]].append(card[1])

        else:
            ranks[card[0]] = [card[1]]

    if len(ranks.keys()) == 2:
        sizes = []

        for k in ranks.keys():
            sizes.append(len(ranks[k]))

        if sorted(sizes) == [2, 3]:
            return True

    return False


def is_four_kind(cards: list) -> bool:
    """
    Check if the cards are a four kind
    """
    cards = sort_hand(cards)
    d = {}

    for card in cards:
        if card[0] in d.keys():
            d[card[0]] += 1

        else:
            d[card[0]] = 1

    return sorted(d.values()) == [1, 4]


def is_straight_flush(cards: list) -> bool:
    """
    Check if the cards are a straight flush
    """
    cards = sort_hand(cards)
    return is_straight(cards) and is_flush(cards)


def is_higher_play(is_this_higher: list, than_this: list):
    if len(is_this_higher) == 1:
        return get_card_score(is_this_higher) > get_card_score(than_this)

    elif len(is_this_higher) == 2:
        return get_pair_score(is_this_higher) > get_pair_score(than_this)

    elif len(is_this_higher) == 3:
        return get_triple_score(is_this_higher) > get_triple_score(than_this)


def get_card_score(card: str) -> int:
    """
    Get the score of a card
    """
    return RANK_ORDER.index(card[0]), SUIT_ORDER.index(card[1])


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


def is_higher_five(is_this_higher: list, than_this: list) -> bool:
    """
    Check if this is a higher five
    """
    pass
