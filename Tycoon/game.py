from Objects.utils import *
from Objects.deck import *


if __name__ == "__main__":
<<<<<<< Updated upstream
    # main game loop
    pass
=======
    card_list = ["KS", "KH", "KD"]
    print(is_triple(card_list))
    card_list = ["ZR", "KH", "KD"]
    print(is_triple(card_list))
    card_list = ["ZR", "ZB", "KD"]
    print(is_triple(card_list))
    card_list = ["ZR", "AS", "KD"]
    print(is_triple(card_list))
    card_list = ["8S", "8H", "8D"]
    print(is_eight_stop(card_list))
    card_list = ["8S", "8H"]
    print(is_eight_stop(card_list))
    card_list = ["8S", "ZB"]
    print(is_eight_stop(card_list))
    card_list = ["8S"]
    print(is_eight_stop(card_list))
    card_list = ["9S"]
    print(is_eight_stop(card_list))
    
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
>>>>>>> Stashed changes
    