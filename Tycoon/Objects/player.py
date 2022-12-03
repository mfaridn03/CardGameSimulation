from Objects.utils import sort_hand
from typing import Optional, List


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.order = -1

    def play(self, is_start_of_round, play_to_beat, round_history, hand_sizes, scores, round_no, is_rev) -> Optional[List]:
        pass
