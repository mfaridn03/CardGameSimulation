# Bot logic for player A
# LOGIC: play the lowest possible play except for round start
from objectss.player import Player
from objectss.utils import *

import typing
import itertools


class PlayerA(Player):
    def __init__(self):
        super().__init__("A")

    def test(self, isor, ptb):
        if isor:
            valid_single_play = [self.hand[0]]
        else:
            valid_single_play = [card for card in self.hand if is_higher_play([card], ptb)]
            
        return [valid_single_play[0]]

    def play(
        self,
        is_start_of_round,
        play_to_beat,
        round_history,
        hand_sizes,
        scores,
        round_no,
    ):
        # must return None or a list of Card objects where None is a pass
        # will throw error if not valid
        possible_plays = self.test(is_start_of_round, play_to_beat)
        return possible_plays
