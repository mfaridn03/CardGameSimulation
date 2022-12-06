# Bot logic for player A
from Objects.player import Player
from Objects.utils import *


class PlayerC(Player):
    def __init__(self):
        super().__init__("A")

    def test(self, isor, ptb, is_rev) -> list:
        # TODO: Define a util function to take a list of cards and pick the lowest value possible play, or otherwise pass
        # Must account for revolutions
        
        sort_hand(self.hand, is_rev)
        if isor:
            return ["3D"]
        if ptb == []:
            valid_single_play = [self.hand[0]]
        else:
            valid_single_play = [card for card in self.hand if is_higher_play([card], ptb, is_rev)]
        
        if valid_single_play == []:
            return []
        else:
            return [valid_single_play[0]]

    def play(
        self,
        is_start_of_round,
        play_to_beat,
        round_history,
        hand_sizes,
        scores,
        round_no,
        is_rev
    ):
        # must return None or a list of Card objects where None is a pass
        # will throw error if not valid
        possible_plays = self.test(is_start_of_round, play_to_beat, is_rev)
        return possible_plays
