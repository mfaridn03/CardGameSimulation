from Objects.utils import *
from Objects.deck import *


# Run some tests here
if __name__ == "__main__":
    card_list = ["KS", "KH", "KD"]
    print(is_triple(card_list))
    card_list = ["ZR", "KH", "KD"]
    print(is_triple(card_list))
    card_list = ["ZR", "ZB", "KD"]
    print(is_triple(card_list))
    card_list = ["ZR", "AS", "KD"]
    print(is_triple(card_list))
    
    deck_test = Deck()
    print(deck_test.__str__())
    deck_test.shuffle()
    
    hands = [[], [], [], []]
    i = 0
    while (not deck_test.is_empty()):
        i = (i + 1) % 4
        hands[i].append(deck_test.deal())
        
    print(hands)
    for hand in hands:
        sort_hand(hand)
        print(hand)
    