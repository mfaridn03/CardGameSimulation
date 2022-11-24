from objectss.consts import SUIT_ORDER, RANK_ORDER
from objectss.utils import sort_hand
from typing import Optional, List


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.order = -1

    def sort_hand(self) -> None:
        # Sort the cards in the hand
        # Suit order: D C H S
        # Rank order: 3 4 5 6 7 8 9 10 J Q K A 2
        sort_hand(self.hand)

    def play(self, is_start_of_round, play_to_beat, round_history, hand_sizes, scores, round_no) -> Optional[List]:
        pass
