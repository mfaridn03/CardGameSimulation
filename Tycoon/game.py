from Objects.utils import *
from Objects.deck import *
from Objects.player import *

class Game:
    def __init__(self, playerlist: typing.List[Player]):
        self.deck = Deck()
        self.deck.shuffle()
        self.data = {
            "is_start_of_round": True,
            "play_to_beat": [],
            "round_history": [[]],
            "hand_sizes": [0, 0, 0, 0],
            "scores": [0, 0, 0, 0],
            "round_no": 0,
            "is_rev": False,
        }
        self.trick_end = False
        self.round_end = False
        self.game_end = False
        self.last_round_victor = None

        self.playerlist = playerlist    # may have more than 4 players

    def deal(self):

    def init_game(self):

    def play_text_based(self):

    def play_round(self):


if __name__ == "__main__":
    # main game loop
    pass
